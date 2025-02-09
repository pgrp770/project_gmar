from typing import List, Dict

import pandas as pd


def read_from_csv_to_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path, encoding="latin1")


def fill_empty_cells(fillna_dict: Dict, df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(fillna_dict)


def create_sub_table(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns].copy()


def create_sub_table_with_id(df: pd.DataFrame, columns: List[str], object_name: str) -> pd.DataFrame:
    sub_table = create_sub_table(df, columns)
    sub_table[f'{object_name}_id'] = range(1, len(sub_table) + 1)
    return sub_table


def add_id_to_table(df: pd.DataFrame) -> pd.DataFrame:
    df['id'] = range(1, len(df) + 1)
    return df


def map_id(df: pd.DataFrame, key, object_name: str) -> Dict[List, int]:
    return df.set_index(key)[f'{object_name}_id'].to_dict()


def add_id_column_to_table_with_map(df: pd.DataFrame, map_ids: Dict, key: str, object_name: str) -> pd.DataFrame:
    def get_id(row):
        return map_ids.get(row[key], None)

    df[f"{object_name}_id"] = df.apply(get_id, axis=1)
    return df


def add_id_columns_to_table_with_map(df: pd.DataFrame, map_ids: Dict, keys: List, object_name: str) -> pd.DataFrame:
    def get_id(row):
        return map_ids.get(tuple([row[key] for key in keys]), None)

    df[f"{object_name}_id"] = df.apply(get_id, axis=1)
    return df


def combine_columns(df: pd.DataFrame, columns: List, new_column_name:str) -> pd.DataFrame:
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
