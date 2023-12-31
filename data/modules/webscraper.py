
from apify_client import ApifyClient
import json

def google_store(country, limit):
    client = ApifyClient(
        token='apify_api_dPdcbf6nqOnroEBpchTDkud3zPoOH24qQnKF')
    input_data = {
        "action": "getApps",
        "num": limit,
        "sort": "NEWEST",
        "lang": "en",
        "country": country,
        "category": "HEALTH_AND_FITNESS",
        "fullDetail": True,
        "search": "google",
    }
    # print("Before client.actor")
    run = client.actor(
        "bebity/google-play-api").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    apps = dataset.list_items().items
    file_path = "google-apps.json"
    # Load existing data from the file if it exists
    existing_data = []
    try:
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        pass

    # Append the new data to the existing data
    existing_data.extend(apps)

    # Write the combined data back to the file
    with open(file_path, "w") as json_file:
        json.dump(existing_data, json_file, indent=3)
    return

def app_store(country, limit):
    client = ApifyClient(
        token='apify_api_dPdcbf6nqOnroEBpchTDkud3zPoOH24qQnKF')
    input_data = {
        "action": "getApps",
        "num": limit,
        "sort": "RECENT",
        "lang": "en",
        "country": country,
        "category": "HEALTH_AND_FITNESS",
        "fullDetail": True,
        "search": "google",
    }
    # print("Before client.actor")
    run = client.actor(
        "bebity/apple-store-api").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    apps = dataset.list_items().items
    file_path = "apple-apps.json"
    with open(file_path, "w") as json_file:
        json.dump(apps, json_file, indent=3)
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
