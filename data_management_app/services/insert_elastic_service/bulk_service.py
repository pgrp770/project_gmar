from typing import List


def from_list_to_actions(index: str, objects: List[dict]) -> List[dict]:
    return [
        {
            "_index": index,
            "_source": action_object
        }
        for action_object in objects
    ]
