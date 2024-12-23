import pytest
from data_management_app.services.normalize_data_srevices.merge_csv_service import *
from data_management_app.config.root_dir import CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE
from data_management_app.utils.pandas_utils import read_from_csv_to_df


@pytest.fixture(scope='module')
def main_table():
    return read_from_csv_to_df(CSV_DATA_MAIN_TABLE)

@pytest.fixture(scope='module')
def second_table():
    return read_from_csv_to_df(CSV_DATA_SECOND_TABLE)


def test_combine_date_columns(main_table):
    result = combine_date_columns_main_table(main_table)
    assert "date" in result.columns


def test_rename_columns_second_table_for_merging(second_table):
    result = rename_columns_second_table_for_merging(second_table)
    assert "date" in result.columns
    assert "Country" not in result.columns
    assert "Perpetrator" not in result.columns
    assert "nkill" in result.columns


def test_merge_tables(main_table, second_table):
    result = merge_tables(main_table, second_table)
    assert len(result) == 6000


def test_process_main_table():
    result = process_main_table(CSV_DATA_MAIN_TABLE)
    assert "date" in result.columns

def test_process_secondary_table():
    result = process_secondary_table(CSV_DATA_SECOND_TABLE)
    assert "Fatalities" not in result.columns


def test_main_flow_merging():
    result = main_flow_merging(CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE)
    assert len(result.columns) == 137
    assert len(result) == 6000