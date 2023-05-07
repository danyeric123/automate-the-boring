# Get Your API: https://developer.nytimes.com/
import os
import requests
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ["API_KEY"]
query = "Science"
url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key="
payload = {}
headers = {}
response = requests.get(url + api_key, headers=headers, data=payload)
for i in response.json()["response"]["docs"]:
    print(
f"""Title: {i['headline']['main']}
URL: {i['web_url']}\n"""  # noqa: E122
    )
