from text_search_app.db.elastic_db.database import elastic_client


def search_by_words(index, search_words):



    query = {
        "query": {
            "match": {
                "summary": search_words  # Search the 'summary' field for the words
            }
        }
    }

    # Perform the search
    response = elastic_client.search(index=index, body=query)

    return response['hits']['hits']

def search_by_summary_and_date(index, search_words, start_date, end_date):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "summary": search_words
                        }
                    }
                ],
                "filter": [
                    {
                        "range": {
                            "Date": {
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

    return response['hits']['hits']


def search_by_type(index, search_words, type):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "summary": search_words
                        }
                    },
                    {
                        "match":{
                            "type": type
                        }
                    }
                ],

            }
        }
    }

    response = elastic_client.search(index=index, body=query)

    return response['hits']['hits']

if __name__ == '__main__':

    # print(list(map(lambda x: x['_source'], search_by_words(index="summeris", search_words="Store"))))
    # print(list(map(lambda x: x['_source'], search_by_summary_and_date(index="summeris", search_words="Store", start_date="1970-01-09", end_date="1970-01-12"))))
    print(list(map(lambda x: x['_source'], search_by_type(index="summeris", search_words="Store", type="history"))))