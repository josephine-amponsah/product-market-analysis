
from apify_client import ApifyClient
import json

def google_store(country):
    client = ApifyClient(
        token='apify_api_BdgKVIBQfeQk9rBpUdoOlNhBG7484q15CTd0')
    input_data = {
        "action": "getApps",
        "num": 200,
        "appIdOrUrl": "com.google.android.apps.translate",
        "devIdOrUrl": "com.google.android.apps.translate",
        "sort": "NEWEST",
        "lang": "en",
        "country": country,
        "fullDetail": True,
        "search": "google",
    }
    # print("Before client.actor")
    run = client.actor(
        "compass/crawler-google-places").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    hotels = dataset.list_items().items
    file_path = "data/raw_data.json"
    with open(file_path, "w") as json_file:
        json.dump(hotels, json_file)
    return hotels

def app_store(country):
    client = ApifyClient(
        token='apify_api_BdgKVIBQfeQk9rBpUdoOlNhBG7484q15CTd0')
    input_data = {
        "action": "getApps",
        "num": 200,
        "appIdOrUrl": "com.google.android.apps.translate",
        "devIdOrUrl": "com.google.android.apps.translate",
        "sort": "NEWEST",
        "lang": "en",
        "country": country,
        "fullDetail": True,
        "search": "google",
    }
    # print("Before client.actor")
    run = client.actor(
        "compass/crawler-google-places").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    hotels = dataset.list_items().items
    file_path = "data/raw_data.json"
    with open(file_path, "w") as json_file:
        json.dump(hotels, json_file)
    return hotels
    return

def get_details(appId):
    return
def get_pricing(appId):
    return
def get_performance(appId):
    return


def get_apps(category, country):
    # Initialize the ApifyClient with your API token
    client = ApifyClient("<YOUR_API_TOKEN>")

    # Prepare the Actor input
    run_input = {
        "action": "getApps",
        "num": 200,
        "appIdOrUrl": "com.google.android.apps.translate",
        "devIdOrUrl": "com.google.android.apps.translate",
        "sort": "NEWEST",
        "lang": "en",
        "country": "us",
        "fullDetail": False,
        "search": "google",
    }

    # Run the Actor and wait for it to finish
    run = client.actor("7jiXXcm7k1SGt9mFr").call(run_input=run_input)
    return
