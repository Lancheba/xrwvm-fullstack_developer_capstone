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

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
LOCAL_REVIEWS = os.path.join(HERE, "local_reviews.json")


def _load_json_list(pattern, key):
    files = glob.glob(os.path.join(BASE, "database", "data", pattern))
    if not files:
        return []
    with open(files[0], encoding="utf-8") as f:
        data = json.load(f)
    return data[key] if isinstance(data, dict) else data


def _posted_reviews():
    if os.path.exists(LOCAL_REVIEWS):
        with open(LOCAL_REVIEWS, encoding="utf-8") as f:
            return json.load(f)
    return []


def _local_fallback(endpoint):
    """Used only when the Node/Mongo backend is not running."""
    parts = endpoint.rstrip("/").split("/")
    if endpoint.startswith("/fetchReviews/dealer/"):
        dealer_id = int(parts[-1])
        reviews = _load_json_list("*review*.json", "reviews") + _posted_reviews()
        return [r for r in reviews if r.get("dealership") == dealer_id]
    if endpoint.startswith("/fetchDealers"):
        dealers = _load_json_list("*dealer*.json", "dealerships")
        if len(parts) > 2:
            return [d for d in dealers if d.get("state") == parts[2]]
        return dealers
    if endpoint.startswith("/fetchDealer/"):
        dealer_id = int(parts[-1])
        dealers = _load_json_list("*dealer*.json", "dealerships")
        return [d for d in dealers if d.get("id") == dealer_id]
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
        response = requests.post(request_url, json=data_dict, timeout=3)
        return response.json()
    except Exception as err:
        print("Backend not reachable, saving review locally: {}".format(err))
        try:
            data_dict["dealership"] = int(data_dict.get("dealership"))
        except (TypeError, ValueError):
            pass
        reviews = _posted_reviews()
        ids = [r.get("id", 0) for r in reviews]
        ids += [r.get("id", 0) for r in _load_json_list("*review*.json", "reviews")]
        data_dict["id"] = max(ids + [0]) + 1
        reviews.append(data_dict)
        with open(LOCAL_REVIEWS, "w", encoding="utf-8") as f:
            json.dump(reviews, f)
        return data_dict
