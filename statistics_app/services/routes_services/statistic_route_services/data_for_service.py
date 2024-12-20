from typing import List, Dict


def get_id_date_casualties_country_region(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "casualties": attack.kills * 2 + attack.wounds,
            "country": attack.terror_location.city.country.id,
            "region": attack.terror_location.city.country.region.id,
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
            "region": attack.terror_location.city.country.region.id,
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


def get_id_date_country_region_groups_targets(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "country": attack.terror_location.city.country.id,
            "region": attack.terror_location.city.country.region.id,
            "groups": [group.group.name for group in attack.groups],
            "targets": [target.target_type.name for target in attack.target_types]
        }
        for attack in attack_li
    ]


def get_id_groups(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attack_li
    ]


def get_id_date_region_groups_target_types(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
            "target_types": [attack.target_type.name for attack in attack.target_types]
        }
        for attack in attack_li
    ]


def get_id_date_country_region_groups_attack_types(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "date": attack.date,
            "country": attack.terror_location.city.country.id,
            "region": attack.terror_location.city.country.region.id,
            "groups": [group.group.name for group in attack.groups],
            "attack_types": [attack.attack_type.name for attack in attack.attack_types]
        }
        for attack in attack_li
    ]


def get_id_country_region_groups(attack_li: List) -> List[Dict]:
    return [
        {
            "id": attack.id,
            "country": attack.terror_location.city.country.name,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attack_li
    ]
