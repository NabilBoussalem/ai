import requests
import os
import json


api_key = "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"
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(json.dumps(response.json().get("data"), indent=4))

# data = response.json().get("data")
# data_list = data if isinstance(data, list) else []
# print(data_list)

