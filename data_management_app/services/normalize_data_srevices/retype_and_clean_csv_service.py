import toolz as tz

import data_management_app.services.normalize_data_srevices.assets_normalize_data_service as assets
from data_management_app.config.root_dir import CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE
from data_management_app.services.normalize_data_srevices.merge_csv_service import main_flow_merging
from data_management_app.utils.pandas_utils import *
import pandas as pd


def get_only_necessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table(df, assets.columns)


def retype_ids_to_int(df: pd.DataFrame) -> pd.DataFrame:
    [retype_column(df, name, int) for name in assets.retype_id_to_int]
    return df


def add_terror_attack_id_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df["terror_attack_id"] = range(1, len(df) + 1)
    return df


def replace_negative_numbers(column, df: pd.DataFrame) -> pd.DataFrame:
    df[column] = df[column].apply(lambda x: max(x, 0))
    return df


def main_flow_clean_csv():
    return tz.pipe(
        main_flow_merging(CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE),
        get_only_necessary_columns,
        tz.partial(fill_empty_cells, assets.fillna_columns),
        tz.partial(replace_negative_numbers, 'nperps'),
        retype_ids_to_int,
        add_terror_attack_id_to_df
    )
