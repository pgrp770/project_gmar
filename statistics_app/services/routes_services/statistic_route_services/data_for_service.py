from typing import List, Dict
import toolz as tz

def get_id_date_casualties_country_region(attack_li: List) ->  List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "casualties": attack.kills + attack.wounds,
            "country": attack.terror_location.city.country.name,
            "region": attack.terror_location.city.country.region.name,
        }
        for attack in attack_li
    ]

def get_id_date_fatal_groups(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "casualties": attack.kills + attack.wounds,
            "groups": [group.group.name for group in attack.groups]
        }
        for attack in attack_li
    ]

def get_id_date_region(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
        }
        for attack in attack_li
    ]

def get_id_date_region_groups(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attack_li
    ]