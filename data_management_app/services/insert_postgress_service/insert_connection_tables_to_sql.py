from typing import List

from data_management_app.db.sql_db.models import *
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import get_all_generic, \
    insert_many_generic
import data_management_app.services.insert_postgress_service.assets_insert_postgres_service as assets
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
import toolz as tz


def get_map_id_from_models(model):
    l = get_all_generic(model)
    return {model.name: model.id for model in l}


def get_map_id_from_terror_location():
    l: List[TerrorLocation] = get_all_generic(TerrorLocation)
    return {(model.city_id, model.latitude, model.longitude): model.id for model in l}


def get_column_with_attack_id(column: str, row, new_column):
    return {"attack_id": row["attack_id"], new_column: row[column]}


def get_weapon_models_from_row(columns: List[str], row, map_id):
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"weapon_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackWeapon(**x)),
        list
    )


def get_attack_type_models_from_row(columns: List[str], row, map_id):
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"attack_type_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackAttackType(**x)),
        list
    )


def get_target_type_models_from_row(columns: List[str], row, map_id):
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"target_type_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackTargetType(**x)),
        list
    )


def get_group_models_from_row(columns: List[str], row, map_id):
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"group_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackGroup(**x)),
        list
    )


def get_nationality_models_from_row(columns: List[str], row, map_id):
    return tz.pipe(
        [row[name] for name in columns],
        set,
        tz.partial(filter, lambda x: x != "Unknown"),
        tz.partial(map, lambda x: {"nationality_id": map_id[x], "terror_attack_id": row["terror_attack_id"]}),
        tz.partial(map, lambda x: TerrorAttackNationality(**x)),
        list
    )


if __name__ == '__main__':

    attack_type_map_id = get_map_id_from_models(AttackType)
    print("map attack_type")
    target_type_map_id = get_map_id_from_models(TargetType)
    print("map target_type")
    group_map_id = get_map_id_from_models(Group)
    print("map group")
    nationality_map_id = get_map_id_from_models(Nationality)
    print("map nationality")
    df = main_flow_clean_csv().to_dict('records')
    terror_attack_attack_type = []
    terror_attack_target_type = []
    terror_attack_group = []
    terror_attack_nationality = []
    terror_attack_terror_location = []

    for row in df:
        terror_attack_attack_type += get_attack_type_models_from_row(assets.attack_type_column, row, attack_type_map_id)
        terror_attack_target_type += get_target_type_models_from_row(assets.target_type_column, row, target_type_map_id)
        terror_attack_group += get_group_models_from_row(assets.group_column, row, group_map_id)
        terror_attack_nationality += get_nationality_models_from_row(assets.nationality_column, row, nationality_map_id)

    terror_attack_terror_location = tz.pipe(
        terror_attack_terror_location,
        tz.partial(filter, lambda x: x.terror_location_id != "Unknown"),
    )
    a = [terror_attack_attack_type, terror_attack_target_type, terror_attack_group,
         terror_attack_nationality]
    for models in a:
        insert_many_generic(models)
        print(f"{type(models[0])} was inserted")
