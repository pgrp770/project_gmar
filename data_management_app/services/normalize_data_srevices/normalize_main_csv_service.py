from pandas import DataFrame
import toolz as tz

from data_management_app.utils.pandas_utils import *


def normalize_region_table(df: DataFrame) -> DataFrame:
    return create_sub_table(df, ["region", "region_txt"])


def normalize_country_table(df: DataFrame) -> DataFrame:
    return create_sub_table(df, ["region", "country", "country_txt"])


def normalize_city_table(df: DataFrame) -> DataFrame:
    return create_sub_table_with_id(df, ["country", "city"], "city")


def normalize_terror_location_table(df: DataFrame) -> DataFrame:
    return create_sub_table_with_id(df, ["eventid", "city_id", "latitude", "longitude"], "terror_location")


def normalize_attack_type_table(df: DataFrame) -> DataFrame:
    return combine_columns_with_ids(df, [
        [
            "attacktype1",
            "attacktype1_txt",
        ],
        [
            "attacktype2",
            "attacktype2_txt",
        ],
        [
            "attacktype3",
            "attacktype3_txt",
        ]
    ], ["attack_type_id", "attack_type"])


def normalize_weapon_table(df: DataFrame) -> DataFrame:
    return combine_columns_with_ids(df, [
        [
            "weaptype1",
            "weaptype1_txt",
        ],
        [
            "weapsubtype1",
            "weapsubtype1_txt",
        ],
        [
            "weaptype2",
            "weaptype2_txt",
        ],
        [
            "weapsubtype2",
            "weapsubtype2_txt",
        ],
        [
            "weaptype3",
            "weaptype3_txt",
        ],
        [
            "weapsubtype3",
            "weapsubtype3_txt",
        ],
        [
            "weaptype4",
            "weaptype4_txt",
        ],
        [
            "weapsubtype4",
            "weapsubtype4_txt",
        ]
    ], ["attack_type_id", "attack_type"])


def normalize_target_type_table(df: DataFrame) -> DataFrame:
    return combine_columns_with_ids(df, [
        [
            "targtype1",
            "targtype1_txt",
        ],
        [
            "targtype2",
            "targtype2_txt",
        ],
        [
            "targtype3",
            "targtype3_txt",
        ],
        [
            "targsubtype1",
            "targsubtype1_txt",
        ],
        [
            "targsubtype2",
            "targsubtype2_txt",
        ],
        [
            "targsubtype3",
            "targsubtype3_txt",
        ]

    ], ["target_type_id", "target_type"])


def normalize_nationality_table(df: DataFrame) -> DataFrame:
    return combine_columns_with_ids(df, [
        [
            "natlty1",
            "natlty1_txt"
        ],
        [
            "natlty2",
            "natlty2_txt",
        ],
        [
            "natlty3",
            "natlty3_txt",
        ],
    ], ["nationality_id", "nationality"])


def normalize_group_table(df: DataFrame) -> DataFrame:
    return tz.pipe(
        combine_columns(df, [
            "gname",
            "gname2",
            "gname3"
        ], "group_name"),
        lambda x: create_ids(x, "group"),
    )


def apply_city_id_on_main_csv(df: DataFrame, cities: DataFrame) -> DataFrame:
    map_id_cities = map_id(cities, "city", "city")
    return add_id_column_to_table_with_map(df, map_id_cities, "city", "city")
