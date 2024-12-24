import toolz as tz

from data_management_app.utils.pandas_utils import *


def normalize_terror_attack_table(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table(df,
                            ["date", "nkill", "nwound", "nperps", "summary", "terror_attack_id", "terror_location_id"])


def normalize_region_table(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table(df, ["region", "region_txt"])


def normalize_country_table(df: pd.DataFrame) -> pd.DataFrame:
    return tz.pipe(
        create_sub_table(df, ["region", "country_txt"])
        .dropna()
        .drop_duplicates(subset="country_txt", keep='first', inplace=False),
        add_id_to_table
    )


def apply_country_id_on_main_csv(df: pd.DataFrame, countries: pd.DataFrame) -> pd.DataFrame:
    map_id_countries = map_id(countries, "country_txt", "country")
    return add_id_column_to_table_with_map(df, map_id_countries, "country_txt", "country")


def normalize_city_table(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table_with_id(df, ["country_id", "city"], "city").drop_duplicates('city')


def apply_city_id_on_main_csv(df: pd.DataFrame, cities: pd.DataFrame) -> pd.DataFrame:
    map_id_cities = map_id(cities, "city", "city")
    return add_id_column_to_table_with_map(df, map_id_cities, "city", "city")


def normalize_terror_location_table(df: pd.DataFrame) -> pd.DataFrame:
    return (create_sub_table_with_id(df, ["city_id", "latitude", "longitude"], "terror_location")
                .dropna()
                .drop_duplicates(
                subset=["city_id", "longitude", "latitude"],
                keep='first', inplace=False)
        )



def normalize_attack_type_table(df: pd.DataFrame) -> pd.DataFrame:
    return tz.pipe(
        combine_columns(df, [
            "attacktype1_txt",
            "attacktype2_txt",
            "attacktype3_txt",

        ], "name"),
        lambda x: create_ids(x, "attack_type"),
    )


def normalize_target_type_table(df: pd.DataFrame) -> pd.DataFrame:
    return tz.pipe(
        combine_columns(df, [
            "targtype1_txt",
            "targtype2_txt",
            "targtype3_txt",
            "targsubtype1_txt",
            "targsubtype2_txt",
            "targsubtype3_txt",

        ], "name"),
        lambda x: create_ids(x, "target_type"),
    )


def normalize_nationality_table(df: pd.DataFrame) -> pd.DataFrame:
    return tz.pipe(
        combine_columns(df, [
            "natlty1_txt",
            "natlty2_txt",
            "natlty3_txt",

        ], "name"),
        lambda x: create_ids(x, "nationality"),
    )


def normalize_group_table(df: pd.DataFrame) -> pd.DataFrame:
    return tz.pipe(
        combine_columns(df, [
            "gname",
            "gname2",
            "gname3"
        ], "name"),
        lambda x: create_ids(x, "group"),
    )



def apply_terror_location_id_on_main_csv(df: pd.DataFrame, terror_location: pd.DataFrame) -> pd.DataFrame:
    map_id_terror_location = map_id(terror_location, ["city_id", "longitude", "latitude"], "terror_location")
    return add_id_columns_to_table_with_map(df, map_id_terror_location, ["city_id", "longitude", "latitude"],
                                            "terror_location")
