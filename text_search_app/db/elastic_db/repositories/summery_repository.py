from text_search_app.db.elastic_db.database import elastic_client
import toolz as tz

import text_search_app.db.elastic_db.repositories.repository_assets as assets


def search_by_words(index, search_words):
    query = assets.search_by_words_query(search_words)
    response = elastic_client.search(index=index, body=query)
    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)


def search_by_category(index, search_words, category):
    query = assets.search_by_category_query(search_words, category)
    response = elastic_client.search(index=index, body=query)
    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)


def search_by_summary_and_date(index, search_words, start_date, end_date):
    query = assets.search_by_summary_and_date_query(search_words, start_date, end_date)
    response = elastic_client.search(index=index, body=query)
    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)
