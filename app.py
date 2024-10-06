from flask import Flask

from classify import classify

from sentiment import get_sentiment
from summarize import summarize_article
from tagging import generate_tags
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def predict(article):
    article['summary'] = summarize_article(article['content'])
    article['sentiment'] = get_sentiment(article['summary'])
    article['tags'] = generate_tags(article['summary'])
    article['classification'] = classify(article['content'])

if __name__ == '__main__':
    app.run(debug=True)
