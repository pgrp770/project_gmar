from typing import List


def from_list_to_actions(index: str ,actions: List[dict]) -> List[dict]:
    return [
        {
            "_index": index,
            "_source": action
        }
        for action in actions
    ]
