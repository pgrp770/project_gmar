import pandas as pd
import toolz as tz
from config.root_dir import CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE
from data_management_app.utils.pandas_utils import read_from_csv


def merge_year_month_day_cells_to_date(df: pd.DataFrame) -> pd.DataFrame:
    df['imonth'] = df['imonth'].replace(0, 1)
    df['iday'] = df['iday'].replace(0, 1)
    df['Date'] = pd.to_datetime(
        df[['iyear', 'imonth', 'iday']].rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}))
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df


def fix_first_table_format(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df


def fix_second_table_format(df: pd.DataFrame) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
    return df


def rename_columns_second_table_for_merging(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
        'Date': 'Date',  # Match the new Date column in table1
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


def flow_first_table(path:str) -> pd.DataFrame:
    return tz.pipe(
        read_from_csv(path),
        merge_year_month_day_cells_to_date,
        fix_first_table_format
    )

def flow_second_table(path:str) -> pd.DataFrame:
    return tz.pipe(
        read_from_csv(path),
        fix_second_table_format,
        rename_columns_second_table_for_merging
    )
def main_flow_merging() -> pd.DataFrame:
    return pd.concat([flow_first_table(CSV_DATA_MAIN_TABLE), flow_second_table(CSV_DATA_SECOND_TABLE)], ignore_index=True)



if __name__ == '__main__':
    print(main_flow_merging())