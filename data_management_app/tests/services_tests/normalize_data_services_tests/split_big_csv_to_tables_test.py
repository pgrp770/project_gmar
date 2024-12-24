import pytest

from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *


@pytest.fixture(scope='module')
def clean_table():
    return main_flow_clean_csv()


@pytest.fixture(scope='module')
def clean_table_with_region_id():
    return pd.DataFrame({
        'date': ['1970-01-01', '1970-01-02'],
        'country': [1, 2],
        'country_txt': ['Country A', 'Country B'],
        'region': [1, 2],
        'region_txt': ['Region A', 'Region B'],
        'city': ['City A', 'City B'],
        'latitude': [34.05, 36.16],
        'longitude': [-118.25, -115.14],
        'summary': ['Attack summary A', 'Attack summary B'],
        'attacktype1_txt': ['Type A', 'Type B'],
        'attacktype2_txt': [None, None],
        'attacktype3_txt': [None, None],
        'targtype1_txt': ['Target A', 'Target B'],
        'targtype2_txt': [None, None],
        'targtype3_txt': [None, None],
        'targsubtype1_txt': [None, None],
        'targsubtype2_txt': [None, None],
        'targsubtype3_txt': [None, None],
        'natlty1_txt': ['Nationality A', 'Nationality B'],
        'natlty2_txt': [None, None],
        'natlty3_txt': [None, None],
        'gname': ['Group A', 'Group B'],
        'gname2': [None, None],
        'gname3': [None, None],
        'nperps': [0, 1],
        'nkill': [1, 2],
        'nwound': [3, 4],
        'terror_attack_id': [101, 102]
    })


@pytest.fixture(scope='module')
def country_df():
    return pd.DataFrame({
        'region': [1, 2],
        'country_txt': ['Country A', 'Country B'],
        'country_id': [10, 20]
    })


@pytest.fixture(scope='module')
def main_df_with_country_id(clean_table_with_region_id, country_df):
    return apply_country_id_on_main_csv(
        df=clean_table_with_region_id,
        countries=country_df
    )


@pytest.fixture(scope='module')
def city_df(main_df_with_country_id):
    return normalize_city_table(main_df_with_country_id)


@pytest.fixture(scope='module')
def main_df_with_city_id(main_df_with_country_id, city_df):
    return apply_city_id_on_main_csv(main_df_with_country_id, city_df)


@pytest.fixture(scope='module')
def terror_location_df(main_df_with_city_id):
    return normalize_terror_location_table(main_df_with_city_id)


@pytest.fixture(scope='module')
def main_df_with_terror_location_id(main_df_with_city_id, terror_location_df):
    return apply_terror_location_id_on_main_csv(main_df_with_city_id, terror_location_df)


def test_normalize_region_table(clean_table):
    result = normalize_region_table(clean_table)
    assert "region" in result.columns


def test_normalize_country_table(clean_table):
    result = normalize_country_table(clean_table)
    assert "country_txt" in result.columns


def test_apply_country_id_on_main_csv(clean_table_with_region_id, country_df):
    result = apply_country_id_on_main_csv(clean_table_with_region_id, country_df)
    assert "country_id" in result


def test_normalize_city_table(main_df_with_country_id):
    result = normalize_city_table(main_df_with_country_id)
    assert "city" in result.columns


def test_apply_city_id_on_main_csv(main_df_with_country_id, city_df):
    result = apply_city_id_on_main_csv(main_df_with_country_id, city_df)
    assert "city_id" in result


def test_normalize_terror_location_table(main_df_with_city_id):
    result = normalize_terror_location_table(main_df_with_city_id)
    assert "city_id" in result.columns


def test_apply_terror_location_id_on_main_csv(main_df_with_city_id, terror_location_df):
    result = apply_terror_location_id_on_main_csv(main_df_with_city_id, terror_location_df)
    assert "terror_location_id" in result


def test_normalize_attack_type_table(main_df_with_terror_location_id):
    result = normalize_attack_type_table(main_df_with_terror_location_id)


def test_normalize_target_type_table(main_df_with_terror_location_id):
    result = normalize_target_type_table(main_df_with_terror_location_id)
    assert "name" in result.columns


def test_normalize_nationality_table(main_df_with_terror_location_id):
    result = normalize_nationality_table(main_df_with_terror_location_id)
    assert "name" in result.columns


def test_normalize_group_table(main_df_with_terror_location_id):
    result = normalize_group_table(main_df_with_terror_location_id)
    assert "name" in result.columns


def test_normalize_terror_attack_table(main_df_with_terror_location_id):
    result = normalize_terror_attack_table(main_df_with_terror_location_id)
    assert "date" in result.columns
