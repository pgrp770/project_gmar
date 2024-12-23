from text_search_app.db.elastic_db.database import elastic_client
import toolz as tz


def search_by_words(index, search_words):
    query = {
        "query": {
            "match": {
                "content": search_words
            }
        }
    }

    response = elastic_client.search(index=index, body=query)

    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)


def search_by_summary_and_date(index, search_words, start_date, end_date):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "content": search_words
                        }
                    }
                ],
                "filter": [
                    {
                        "range": {
                            "date": {
                                "gte": start_date,
                                "lte": end_date
                            }
                        }
                    }
                ]
            }
        }
    }

    response = elastic_client.search(index=index, body=query)

    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)


def search_by_type(index, search_words, typo):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "content": {
                                "query": search_words,
                                "fuzziness": "AUTO"  # Adjust fuzziness level as needed
                            }
                        }
                    },
                    {
                        "term": {
                            "category.keyword": typo
                        }
                    }
                ]
            }
        }
    }

    response = elastic_client.search(index=index, body=query)

    return tz.pipe(
        response['hits']['hits'],
        tz.partial(map, lambda x: x['_source']),
        list)


if __name__ == '__main__':
    print(search_by_type("summeris", "Asia's", "historical terror attack"))
