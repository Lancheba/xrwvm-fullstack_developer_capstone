import os
import json
import glob
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def _local_fallback(endpoint):
    """Used only when the Node/Mongo backend is not running."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if endpoint.startswith("/fetchReviews/dealer/"):
        dealer_id = int(endpoint.rstrip("/").split("/")[-1])
        files = glob.glob(os.path.join(base, "database", "data", "*review*.json"))
        if not files:
            return []
        with open(files[0], encoding="utf-8") as f:
            data = json.load(f)
        reviews = data["reviews"] if isinstance(data, dict) else data
        return [r for r in reviews if r.get("dealership") == dealer_id]
    return []


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
    request_url = backend_url + endpoint + ("?" + params if params else "")
    print("GET from {}".format(request_url))
    try:
        response = requests.get(request_url, timeout=3)
        return response.json()
    except Exception:
        print("Backend not reachable, using local data")
        return _local_fallback(endpoint)


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url, timeout=3)
        return response.json()
    except Exception as err:
        print("Sentiment service unavailable: {}".format(err))
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except Exception as err:
        print("Network exception occurred: {}".format(err))
