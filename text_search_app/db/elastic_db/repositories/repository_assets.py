def search_by_words_query(search_words):
    return {
        "size": 1000,
        "query": {
            "match": {
                "content": {
                    "query": search_words,
                    "fuzziness": "AUTO"
                }
            }
        }
    }


def search_by_summary_and_date_query(search_words, start_date, end_date):
    return {
        "size": 1000,
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


def search_by_category_query(search_words, category):
    return {
        "size": 1000,
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "content": {
                                "query": search_words,
                                "fuzziness": "AUTO"
                            }
                        }
                    },
                    {
                        "term": {
                            "category.keyword": category
                        }
                    }
                ]
            }
        }
    }