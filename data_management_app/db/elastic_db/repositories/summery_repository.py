from typing import List

from elasticsearch.helpers import bulk

from data_management_app.db.elastic_db.database import elastic_client


def create_bulk(summeries_actions: List[dict]):
    try:
        print(f"creating {len(summeries_actions)} summeries in {summeries_actions[0]['_index']}")
        return bulk(elastic_client, summeries_actions)
    except:
        return None
