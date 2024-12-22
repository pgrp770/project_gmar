import toolz as tz
from data_management_app.services.normalize_data_srevices.merge_csv_service import main_flow_merging
from data_management_app.utils.pandas_utils import *
import pandas as pd
columns = [
    "Date",
    "country",
    "country_txt",
    "region",
    "region_txt",
    "city",
    "latitude",
    "longitude",
    "summary",
    "attacktype1_txt",
    "attacktype2_txt",
    "attacktype3_txt",
    "targtype1_txt",
    "targtype2_txt",
    "targtype3_txt",
    "targsubtype1_txt",
    "targsubtype2_txt",
    "targsubtype3_txt",
    "natlty1_txt",
    "natlty2_txt",
    "natlty3_txt",
    "gname",
    "gname2",
    "gname3",
    "nperps",
    # "weaptype1_txt",
    # "weapsubtype1_txt",
    # "weaptype2_txt",
    # "weapsubtype2_txt",
    # "weaptype3_txt",
    # "weapsubtype3_txt",
    # "weaptype4_txt",
    # "weapsubtype4_txt",
    "nkill",
    "nwound",
]
fillna_columns_with_empty_string=[
    "region_txt"
]
fillna_columns_with_unknown={
    # 'weaptype1_txt':'Unknown',
    # 'weapsubtype1_txt':'Unknown',
    # 'weaptype2_txt':'Unknown',
    # 'weapsubtype2_txt':'Unknown',
    # 'weaptype3_txt':'Unknown',
    # 'weapsubtype3_txt':'Unknown',
    # 'weaptype4_txt':'Unknown',
    # 'weapsubtype4_txt':'Unknown',
    "targtype1_txt": "Unknown",
    "targtype2_txt": "Unknown",
    "targtype3_txt": "Unknown",
    "targsubtype1_txt": "Unknown",
    "targsubtype2_txt": "Unknown",
    "targsubtype3_txt": "Unknown",
    "attacktype1_txt":"Unknown",
    "attacktype2_txt":"Unknown",
    "attacktype3_txt":"Unknown",
    "gname":"Unknown",
    "gname2":"Unknown",
    "gname3":"Unknown",
    "natlty1_txt":"Unknown",
    "natlty2_txt":"Unknown",
    "natlty3_txt":"Unknown",
    "latitude":0,
    "longitude":0,
}
fillna_columns_with_zero = [
    "country",
    "region",
    "nkill",
    "nwound",
    "nperps"
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
def replace_negative_numbers(column, df: pd.DataFrame) -> pd.DataFrame:
    df[column] = df[column].apply(lambda x: max(x, 0))
    return df
def main_flow_clean_csv():
    return tz.pipe(
        main_flow_merging(),
        get_only_necessary_columns,
        tz.partial(fill_empty_cells_in_with_zeros, fillna_columns_with_zero),
        lambda df: df.fillna(fillna_columns_with_unknown),
        tz.partial(replace_negative_numbers, 'nperps'),
        retype_ids_to_int,
        add_terror_attack_id_to_df
    )

if __name__ == '__main__':
    df=main_flow_clean_csv()
    print(df)

