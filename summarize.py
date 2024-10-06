import requests
import json

def summarize_article(article_content):
    url = 'http://10.0.0.210:3000/summarize'
    payload = {
        "body": article_content
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to summarize article. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}