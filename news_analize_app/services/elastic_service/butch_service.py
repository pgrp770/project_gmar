from typing import List


def from_list_to_actions(sumeries:List[dict]) -> List[dict]:
    return [
        {
            "_index": "summeris",
            "_source": summery
        }
        for summery in sumeries
    ]

