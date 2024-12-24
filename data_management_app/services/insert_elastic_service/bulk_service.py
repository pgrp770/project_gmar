from typing import List
import toolz as tz

def from_list_to_actions_with_chunks(index: str, objects: List[dict]) -> List[List[dict]]:
    breakpoint()
    data = [
        {
            "_index": index,
            "_source": action_object
        }
        for action_object in objects
    ]
    return list(tz.partition_all(1000, data))


def from_list_to_actions(index: str, objects: List[dict]) -> List[dict]:
    return [
        {
            "_index": index,
            "_source": action_object
        }
        for action_object in objects
    ]

