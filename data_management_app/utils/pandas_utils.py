from typing import List, Dict
import toolz as t

import pandas as pd


def read_from_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, encoding="latin1")


def remove_empty_columns_and_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(how='all').dropna(axis=1, how='all')


def remove_row_by_empty_columns(empty_columns: List[str], df) -> pd.DataFrame:
    return df.dropna(subset=empty_columns, how='any')


def fill_empty_cells(fillna_dict: Dict, df):
    return df.fillna(fillna_dict)


def flow_first_normalize(path: str, empty_columns: List = [], fillna_dict: Dict = {}) -> pd.DataFrame:
    return t.pipe(
        read_from_csv(path),
        # remove_empty_columns_and_rows,
        t.partial(remove_row_by_empty_columns, empty_columns),
        t.partial(fill_empty_cells, fillna_dict)
    )


def create_sub_table(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns].copy()


def create_sub_table_with_id(df: pd.DataFrame, columns: List[str], object_name: str) -> pd.DataFrame:
    sub_table = create_sub_table(df, columns)
    sub_table[f'{object_name}_id'] = range(1, len(sub_table) + 1)
    return sub_table


def map_id(df: pd.DataFrame, key: str, object_name: str) -> Dict[List, int]:
    return df.set_index(key)[f'{object_name}_id'].to_dict()


def add_id_column_to_table_with_map(df: pd.DataFrame, map_ids: Dict, key: str, object_name: str) -> pd.DataFrame:
    def get_id(row):
        return map_ids.get(row[key], None)

    df[f"{object_name}_id"] = df.apply(get_id, axis=1)
    return df


def combine_columns_with_ids(df, groups: List[List], new_column_names):
    combined_rows = []

    for id_col, name_col in groups:
        temp_df = df[[id_col, name_col]].dropna(how="all")
        temp_df.columns = new_column_names
        combined_rows.append(temp_df)

    combined_df = pd.concat(combined_rows, ignore_index=True).drop_duplicates()

    return combined_df


def combine_columns(df, columns, new_column_name):
    melted = pd.melt(df, value_vars=columns, value_name=new_column_name)
    return pd.DataFrame(
        melted[new_column_name]
        .drop_duplicates()
        .reset_index(drop=True),
        columns=[new_column_name]
    )


def create_ids(df: pd.DataFrame, object_name: str) -> pd.DataFrame:
    df[f'{object_name}_id'] = range(1, len(df) + 1)
    return df


def retype_column(df: pd.DataFrame, column_name: str, target_type: type, fill_value=0) -> pd.DataFrame:

    df[column_name] = df[column_name].fillna(fill_value).apply(lambda x: target_type(x))
    return df