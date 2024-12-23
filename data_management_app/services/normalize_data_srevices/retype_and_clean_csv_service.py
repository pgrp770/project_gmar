import toolz as tz

import data_management_app.services.normalize_data_srevices.assets_normalize_data_service as assets
from data_management_app.services.normalize_data_srevices.merge_csv_service import main_flow_merging
from data_management_app.utils.pandas_utils import *
import pandas as pd


def get_only_necessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table(df, assets.columns)


def fill_empty_cells_in_with_zeros(list_columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return fill_empty_cells({name: 0 for name in list_columns}, df)


def fill_empty_cells_in_with_empty_string(list_columns: List[str], df: pd.DataFrame) -> pd.DataFrame:
    return fill_empty_cells({name: '' for name in list_columns}, df)


def retype_ids_to_int(df: pd.DataFrame) -> pd.DataFrame:
    [retype_column(df, name, int) for name in assets.fillna_columns_with_zero]
    return df


def add_terror_attack_id_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df["terror_attack_id"] = range(1, len(df) + 1)
    return df


def replace_negative_numbers(column, df: pd.DataFrame) -> pd.DataFrame:
    df[column] = df[column].apply(lambda x: max(x, 0))
    return df


def main_flow_clean_csv():
    return tz.pipe(
        main_flow_merging(),
        get_only_necessary_columns,
        tz.partial(fill_empty_cells_in_with_zeros, assets.fillna_columns_with_zero),
        lambda df: df.fillna(assets.fillna_columns_with_unknown),
        tz.partial(replace_negative_numbers, 'nperps'),
        retype_ids_to_int,
        add_terror_attack_id_to_df
    )
