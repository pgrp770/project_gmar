from typing import List
import toolz as tz
from data_management_app.services.normalize_data_srevices.merge_csv_service import main_flow_merging
from data_management_app.utils.pandas_utils import *
import pandas as pd
columns = [
    "eventid",
    "Date",
    "country",
    "country_txt",
    "region",
    "region_txt",
    "provstate",  # ארגון מודיעין
    "city",
    "latitude",
    "longitude",
    "location",
    "summary",
    "success",
    "suicide",
    "attacktype1",
    "attacktype1_txt",
    "attacktype2",
    "attacktype2_txt",
    "attacktype3",
    "attacktype3_txt",
    "targtype1",
    "targtype1_txt",
    "targtype2",
    "targtype2_txt",
    "targtype3",
    "targtype3_txt",
    "targsubtype1",
    "targsubtype1_txt",
    "targsubtype2",
    "targsubtype2_txt",
    "targsubtype3",
    "targsubtype3_txt",
    "natlty1",
    "natlty1_txt",
    "natlty2",
    "natlty2_txt",
    "natlty3",
    "natlty3_txt",
    "gname",
    "gname2",
    "gname3",
    "motive",
    "nperps",
    "weaptype1",
    "weaptype1_txt",
    "weapsubtype1",
    "weapsubtype1_txt",
    "weaptype2",
    "weaptype2_txt",
    "weapsubtype2",
    "weapsubtype2_txt",
    "weaptype3",
    "weaptype3_txt",
    "weapsubtype3",
    "weapsubtype3_txt",
    "weaptype4",
    "weaptype4_txt",
    "weapsubtype4",
    "weapsubtype4_txt",
    "nkill",
    "nwound",
]
fillna_columns_with_empty_string=[
    "region_txt"
]
fillna_columns_with_zero = [
    "eventid",
    "country",
    "region",
    "attacktype1",
    "attacktype2",
    "attacktype3",
    "targtype1",
    "targtype2",
    "targsubtype1",
    "targsubtype2",
    "natlty1",
    "natlty2",
    "natlty3",
    "weaptype1",
    "weapsubtype1",
    "weaptype2",
    "weapsubtype2",
    "weaptype3",
    "weapsubtype3",
    "weaptype4",
    "weapsubtype4",
    "nkill",
    "nwound",
]

def get_only_necessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    return create_sub_table(df, columns)

def fill_empty_cells_in_with_zeros(list_columns:List[str], df: pd.DataFrame) -> pd.DataFrame:
    return fill_empty_cells({name: 0 for name in list_columns}, df)

def fill_empty_cells_in_with_empty_string(list_columns:List[str], df: pd.DataFrame) -> pd.DataFrame:
    return fill_empty_cells({name: '' for name in list_columns}, df)

def retype_ids_to_int(df: pd.DataFrame) -> pd.DataFrame:
    [retype_column(df, name, int) for name in fillna_columns_with_zero]
    return df

def add_terror_attack_id_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df["terror_attack_id"] = range(1, len(df) + 1)
    return df

def main_flow_clean_csv():
    return tz.pipe(
        main_flow_merging(),
        get_only_necessary_columns,
        tz.partial(fill_empty_cells_in_with_zeros, fillna_columns_with_zero),
        lambda df: df.fillna({"attacktype1_txt":"Unknown", "attacktype2_txt":"Unknown", "attacktype3_txt":"Unknown"}),
        lambda df: df.fillna({"attacktype1":9, "attacktype2":9, "attacktype3":9}),

        retype_ids_to_int,
        add_terror_attack_id_to_df
    )

if __name__ == '__main__':
    df=main_flow_clean_csv()
    print(df)

