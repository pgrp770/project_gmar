from typing import List


def from_list_to_actions(summeries: List[dict]) -> List[dict]:
    return [
        {
            "_index": "summeries",
            "_source": summery
        }
        for summery in summeries
    ]
