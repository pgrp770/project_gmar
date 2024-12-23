import json
import os
import time

import requests
import toolz as tz

def fetch_articles(api_key, keyword, articles_page=1, articles_count=100):
    print("start fetch news")
    url = "https://eventregistry.org/api/v1/article/getArticles"


    # Prepare the request body
    payload = {
        "action": "getArticles",
        "keyword": keyword,
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": articles_page,
        "articlesCount": articles_count,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": ["news", "pr"],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": api_key
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("finish fetch news")
        return response.json()  # Return the JSON response

    else:
        print(f"Error: {response.status_code}")
        return None

def save_json_to_file(data, file_path):
    # Open the file and write the JSON data to it
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")



def process_articles(data):
    if data and "articles" in data:
        for article in data["articles"]:
            title = article.get("title", "No Title")
            url = article.get("url", "No URL")
            date = article.get("date", "No Date")
            body = article.get("body", "No Body")
            print(f"Title: {title}\nURL: {url}\nDate: {date}\nBody: {body}\n")
    else:
        print("No articles found or there was an issue with the data.")


# Main script to fetch and display articles
def main():
    api_key = "7e31d163-3a72-434f-a25b-41ec53fb5e92"  # Replace with your actual API key
    keyword = "terror attack"  # Modify to search for other keywords
    articles_page = 1
    articles_count = 100

    while True:
        # Fetch articles from the API
        data = fetch_articles(api_key, keyword, articles_page, articles_count)
        relative_path = os.path.join("../news_api_project", "data", "articles_data.json")
        save_json_to_file(data, relative_path)


        # Process the fetched articles
        process_articles(data)

        # Wait for 2 minutes before fetching the next page
        articles_page += 1  # Move to the next page
        time.sleep(120)  # Sleep for 2 minutes (120 seconds)




if __name__ == "__main__":
    def read_json_from_file(file_path) -> dict:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    return data
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print(f"File {file_path} not found.")
            return None
    relative_path = os.path.join("../news_api_project", "data", "articles_data.json")


    # print(read_json_from_file(relative_path)['articles']['results'][0].keys())
import json
import os
import time

import requests


def fetch_articles(api_key, keyword, articles_page=1, articles_count=100):
    url = "https://eventregistry.org/api/v1/article/getArticles"

    # Prepare the request body
    payload = {
        "action": "getArticles",
        "keyword": keyword,
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": articles_page,
        "articlesCount": articles_count,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": ["news", "pr"],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": api_key
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    if response.status_code == 200:

        return response.json()  # Return the JSON response

    else:
        print(f"Error: {response.status_code}")
        return None

def save_json_to_file(data, file_path):
    # Open the file and write the JSON data to it
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")



def process_articles(data):
    if data and "articles" in data:
        for article in data["articles"]:
            title = article.get("title", "No Title")
            url = article.get("url", "No URL")
            date = article.get("date", "No Date")
            body = article.get("body", "No Body")
            print(f"Title: {title}\nURL: {url}\nDate: {date}\nBody: {body}\n")
    else:
        print("No articles found or there was an issue with the data.")


# Main script to fetch and display articles
def main():
    print("request articles")
    api_key = "a9acabe7-c5d6-489b-8ea9-c2fd499522b3"  # Replace with your actual API key
    keyword = "terror attack"  # Modify to search for other keywords
    articles_page = 1
    articles_count = 5



    data = fetch_articles(api_key, keyword, articles_page, articles_count)
    return data





if __name__ == "__main__":
    def read_json_from_file(file_path) -> dict:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    return data
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print(f"File {file_path} not found.")
            return None
    relative_path = os.path.join("../../news_analize_app", "data", "articles_data.json")

    a = json.load(read_json_from_file(relative_path)['articles']['results'][0])
    print(a["title"] + a["body"])


