import pandas as pd
import toolz as tz
from data_management_app.config.root_dir import CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE
from data_management_app.utils.pandas_utils import read_from_csv


def combine_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    df['imonth'] = df['imonth'].replace(0, 1)
    df['iday'] = df['iday'].replace(0, 1)
    df['Date'] = pd.to_datetime(
        df[['iyear', 'imonth', 'iday']].rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}))
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df


def normalize_main_table_date(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df


def normalize_second_table_date(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
    return df


def rename_columns_second_table_for_merging(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
        'Date': 'Date',
        'City': 'city',
        'Country': 'country_txt',
        'Perpetrator': 'gname',
        'Weapon': 'weaptype1_txt',
        'Injuries': 'nwound',
        'Fatalities': 'nkill',
        'Description': 'summary'
    }, inplace=True)
    return df


def merge_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)


def process_main_table(path: str) -> pd.DataFrame:
    return tz.pipe(
        read_from_csv(path),
        combine_date_columns,
        normalize_main_table_date
    )


def process_secondary_table(path: str) -> pd.DataFrame:
    return tz.pipe(
        read_from_csv(path),
        normalize_second_table_date,
        rename_columns_second_table_for_merging
    )


def main_flow_merging() -> pd.DataFrame:
    return pd.concat([process_main_table(CSV_DATA_MAIN_TABLE), process_secondary_table(CSV_DATA_SECOND_TABLE)],
                     ignore_index=True)


if __name__ == '__main__':
    print(main_flow_merging())
