import numpy as np
import pytest
import data_management_app.services.normalize_data_srevices.assets_normalize_data_service as assets

from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import *


@pytest.fixture(scope='module')
def table():
    return main_flow_merging(CSV_DATA_MAIN_TABLE, CSV_DATA_SECOND_TABLE)


def test_get_only_necessary_columns(table):
    result = get_only_necessary_columns(table)
    assert "summary" in result.columns
    assert "targsubtype2_txt" in result.columns


def test_retype_ids_to_int(table):
    result = tz.pipe(
        table,
        retype_ids_to_int,
        get_only_necessary_columns
    )
    assert isinstance(result["region"][0], np.int64)


def test_add_terror_attack_id_to_df(table):
    result = tz.pipe(
        table,
        retype_ids_to_int,
        get_only_necessary_columns,
        add_terror_attack_id_to_df
    )
    assert "terror_attack_id" in result.columns


def test_replace_negative_numbers(table):
    result = tz.pipe(

            table,
            retype_ids_to_int,
            get_only_necessary_columns,
            add_terror_attack_id_to_df,

        tz.partial(replace_negative_numbers, 'nperps')
        )
    assert result['nperps'].fillna(0).ge(0).all()
