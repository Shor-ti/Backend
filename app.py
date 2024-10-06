from flask import Flask, request, jsonify

from classify import classify
from db import hindu
from scrapper import get_article_info
from bson.json_util import dumps

from sentiment import get_sentiment
from summarize import summarize_article
from tagging import generate_tags
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ondemand', methods=['POST'])
def get_data():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    existing_article = hindu.find_one({"url": url})
    if existing_article:
        if 'summary' not in existing_article:
            predict(existing_article)
            hindu.update_one({"_id": existing_article["_id"]}, {"$set": existing_article})
        return dumps(existing_article), 200
    article_info = get_article_info(url)
    predict(article_info)
    hindu.insert_one(article_info)
    return dumps(article_info), 201


@app.route('/article/<string:article_id>', methods=['GET'])
def get_article(article_id):
    if not article_id:
        return jsonify({"error": "Article ID is required"}), 400

    try:
        article_id_obj = ObjectId(article_id)
    except Exception as e:
        return jsonify({"error": "Invalid article ID format"}), 400

    existing_article = hindu.find_one({"_id": article_id_obj})

    if existing_article:
        if 'summary' not in existing_article:
            predict(existing_article)
            hindu.update_one({"_id": existing_article["_id"]}, {"$set": existing_article})
        return dumps(existing_article), 200

    return jsonify({"error": "Article not found"}), 404


@app.route('/articles', methods=['GET'])
def get_articles():
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "articles": {
                    "$push": {
                        "title": "$headline",
                        "url": "$url",
                        "_id": "$_id",
                        "image_url": "$image"
                    }
                }
            }
        }
    ]
    grouped_articles = list(hindu.aggregate(pipeline))
    return dumps(grouped_articles), 200

@app.route('/article/<article_id>', methods=['GET'])
def get_article_by_id(article_id):
    try:
        article = hindu.find_one({"_id": ObjectId(article_id)})
        if article:
            return dumps(article), 200
        else:
            return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def predict(article):
    article['summary'] = summarize_article(article['content'])
    article['sentiment'] = get_sentiment(article['summary'])
    article['tags'] = generate_tags(article['summary'])
    article['classification'] = classify(article['content'])

if __name__ == '__main__':
    app.run(debug=True)
