from typing import List, Dict

from data_management_app.db.sql_db.models import *
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
import data_management_app.services.insert_postgress_service.assets_insert_postgres_service as assets
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
import toolz as tz

from data_management_app.utils.postgres_utils import get_map_id_from_models


def get_attack_type_models_from_row(columns: List[str], row: Dict, map_id: Dict) -> List[TerrorAttackAttackType]:
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"attack_type_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackAttackType(**x)),
        list
    )


def get_target_type_models_from_row(columns: List[str], row: Dict, map_id: Dict) -> List[TerrorAttackTargetType]:
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"target_type_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackTargetType(**x)),
        list
    )


def get_group_models_from_row(columns: List[str], row: Dict, map_id: Dict) -> List[TerrorAttackGroup]:
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"group_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackGroup(**x)),
        list
    )


def get_nationality_models_from_row(columns: List[str], row: Dict, map_id: Dict) -> List[TerrorAttackNationality]:
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"nationality_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackNationality(**x)),
        list
    )


def main_flow_insert_connection_tables():

    df = main_flow_clean_csv().to_dict('records')

    attack_type_map_id = get_map_id_from_models(AttackType)
    target_type_map_id = get_map_id_from_models(TargetType)
    group_map_id = get_map_id_from_models(Group)
    nationality_map_id = get_map_id_from_models(Nationality)

    attack_types = [
        model
        for row in df
        for model in get_attack_type_models_from_row(assets.attack_type_column, row, attack_type_map_id)
    ]

    target_types = [
        model
        for row in df
        for model in get_target_type_models_from_row(assets.target_type_column, row, target_type_map_id)
    ]

    groups = [
        model
        for row in df
        for model in get_group_models_from_row(assets.group_column, row, group_map_id)
    ]

    nationalities = [
        model
        for row in df
        for model in get_nationality_models_from_row(assets.nationality_column, row, nationality_map_id)
    ]

    [insert_many_generic(models) for models in [attack_types, target_types, groups, nationalities]]
