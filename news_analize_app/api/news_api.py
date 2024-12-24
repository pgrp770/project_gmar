import time
import requests
from news_analize_app.services.flow_service.analyze_news_service import insert_articles_to_elastic


def fetch_articles(api_key, keyword, articles_page=1, articles_count=100):
    print("start fetch news")
    url = "https://eventregistry.org/api/v1/article/getArticles"

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

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("finish fetch news")
        return response.json()

    else:
        print(f"Error: {response.status_code}")
        return None


def main_flow(articles_count: int = 100, time_sleep: int = 120):
    api_key = "7e31d163-3a72-434f-a25b-41ec53fb5e92"
    keyword = "terror attack"
    articles_page = 1
    articles_count = articles_count

    while True:
        print(f"send {articles_count} articles")
        data = fetch_articles(api_key, keyword, articles_page, articles_count)
        insert_articles_to_elastic(data['articles']['results'])
        articles_page += 1
        time.sleep(time_sleep)
