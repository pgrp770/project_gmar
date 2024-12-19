from pandas import DataFrame
import toolz as tz

from data_management_app.db.sql_db.database import init_db
from data_management_app.db.sql_db.models import Region, Country, City, TerrorLocation
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *
from data_management_app.utils.pandas_utils import *


def insert_region_table_to_postgres(df_region: DataFrame) -> None:
    df_region = pd.concat([df_region, pd.DataFrame({'region': [0], 'region_txt': ['Unknown']})], ignore_index=True)
    return t.pipe(
        df_region.dropna().drop_duplicates(subset=None, keep='first', inplace=False),
        lambda df: df.rename(columns={'region': 'id', 'region_txt': 'region_name'}, inplace=False),
        lambda df: df.to_dict(orient='records'),
        tz.partial(map, lambda x: Region(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_country_table_to_postgres(df_country: DataFrame) -> None:
    df = df_country.dropna().dropna().drop_duplicates(subset="country_txt", keep='first', inplace=False)
    df['id'] = range(1, len(df) + 1)
    return tz.pipe(
        df,
        lambda d: d.rename(columns={'region': 'region_id', 'country_txt': 'country_name'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Country(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


# apply_city_id_on_main_csv,
def insert_city_table_to_postgres(df_city: DataFrame) -> None:
    return tz.pipe(
        df_city.dropna().dropna().drop_duplicates(subset="city", keep='first', inplace=False),
        lambda d: d.rename(columns={'city': 'city_name', 'city_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: City(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_terror_location_to_postgres(df_terror_location: DataFrame) -> None:
    return tz.pipe(
        df_terror_location.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False),
        lambda d: d.rename(columns={'terror_location_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorLocation(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_attack_type(df : DataFrame) -> None:
    return tz.pipe(
        df
    )
#
# def normalize_attack_type_table(df: DataFrame) -> DataFrame:
#     return combine_columns_with_ids(df, [
#         [
#             "attacktype1",
#             "attacktype1_txt",
#         ],
#         [
#             "attacktype2",
#             "attacktype2_txt",
#         ],
#         [
#             "attacktype3",
#             "attacktype3_txt",
#         ]
#     ], ["attack_type_id", "attack_type"])
#
#
# def normalize_weapon_table(df: DataFrame) -> DataFrame:
#     return combine_columns_with_ids(df, [
#         [
#             "weaptype1",
#             "weaptype1_txt",
#         ],
#         [
#             "weapsubtype1",
#             "weapsubtype1_txt",
#         ],
#         [
#             "weaptype2",
#             "weaptype2_txt",
#         ],
#         [
#             "weapsubtype2",
#             "weapsubtype2_txt",
#         ],
#         [
#             "weaptype3",
#             "weaptype3_txt",
#         ],
#         [
#             "weapsubtype3",
#             "weapsubtype3_txt",
#         ],
#         [
#             "weaptype4",
#             "weaptype4_txt",
#         ],
#         [
#             "weapsubtype4",
#             "weapsubtype4_txt",
#         ]
#     ], ["attack_type_id", "attack_type"])
#
#
# def normalize_target_type_table(df: DataFrame) -> DataFrame:
#     return combine_columns_with_ids(df, [
#         [
#             "targtype1",
#             "targtype1_txt",
#         ],
#         [
#             "targtype2",
#             "targtype2_txt",
#         ],
#         [
#             "targtype3",
#             "targtype3_txt",
#         ],
#         [
#             "targsubtype1",
#             "targsubtype1_txt",
#         ],
#         [
#             "targsubtype2",
#             "targsubtype2_txt",
#         ],
#         [
#             "targsubtype3",
#             "targsubtype3_txt",
#         ]
#
#     ], ["target_type_id", "target_type"])
#
#
# def normalize_nationality_table(df: DataFrame) -> DataFrame:
#     return combine_columns_with_ids(df, [
#         [
#             "natlty1",
#             "natlty1_txt"
#         ],
#         [
#             "natlty2",
#             "natlty2_txt",
#         ],
#         [
#             "natlty3",
#             "natlty3_txt",
#         ],
#     ], ["nationality_id", "nationality"])
#
#
# def normalize_group_table(df: DataFrame) -> DataFrame:
#     return tz.pipe(
#         combine_columns(df, [
#             "gname",
#             "gname2",
#             "gname3"
#         ], "group_name"),
#         lambda x: create_ids(x, "group"),
#     )
#
#
# def apply_city_id_on_main_csv(df: DataFrame, cities: DataFrame) -> DataFrame:
#     map_id_cities = map_id(cities, "city", "city")
#     return add_id_column_to_table_with_map(df, map_id_cities, "city", "city")
#
# def apply_groups_id_on_main_csv(df: DataFrame, groups: DataFrame) -> DataFrame:
#     map_id_groups = map_id(groups, "group_name", "group")
#     return tz.pipe(
#         add_id_column_to_table_with_map(df, map_id_groups, "gname", "group1"),
#         lambda x: add_id_column_to_table_with_map(x, map_id_groups, "gname2", "group2"),
#         lambda x: add_id_column_to_table_with_map(x, map_id_groups, "gname3", "group3"),
#     )

def main_flow_insertion_postgres():
    df = main_flow_clean_csv()
    insert_region_table_to_postgres(normalize_region_table(df))

    insert_country_table_to_postgres(normalize_country_table(df))

    df_country = normalize_country_table(df).dropna().dropna().drop_duplicates(subset="country_txt", keep='first',                                                                   inplace=False)
    df_country['country_id'] = range(1, len(df_country) + 1)
    apply_country_id_on_main_csv(df, df_country)

    df_city = normalize_city_table(df).dropna().dropna().drop_duplicates(subset="city", keep='first', inplace=False)
    apply_city_id_on_main_csv(df, df_city)

    insert_city_table_to_postgres(normalize_city_table(df))

    a = normalize_terror_location_table(df)
    insert_terror_location_to_postgres(a)
    df_terror_location = a.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False)
    apply_terror_location_id_on_main_csv(df, df_terror_location)
if __name__ == '__main__':
    # main_flow_insertion_postgres()
    df = main_flow_clean_csv()
    print(normalize_attack_type_table(df))
