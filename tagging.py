import requests
import json


def generate_tags(summary):
    url = 'http://10.0.0.210:3000/tag'
    payload = {
        "body": summary
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to generate tags. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}