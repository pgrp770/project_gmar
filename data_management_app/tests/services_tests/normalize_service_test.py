# import pytest
#
# from data_management_app.config.root_dir import CSV_DATA_MAIN_TABLE
# from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *
# from data_management_app.utils.pandas_utils import *
#
#
# @pytest.fixture(scope='module')
# def clean_table():
#     columns = [
#         "eventid",
#
#         "iyear",
#         "imonth",
#         "iday",
#
#         "country",
#         "country_txt",
#
#         "region",
#         "region_txt",
#
#         "provstate",  # ארגון מודיעין
#         "city",
#         "latitude",
#         "longitude",
#         "location",
#         "summary",
#         "success",
#         "suicide",
#
#         "attacktype1",
#         "attacktype1_txt",
#         "attacktype2",
#         "attacktype2_txt",
#         "attacktype3",
#         "attacktype3_txt",
#
#         "targtype1",
#         "targtype1_txt",
#         "targtype2",
#         "targtype2_txt",
#         "targtype3",
#         "targtype3_txt",
#
#         "targsubtype1",
#         "targsubtype1_txt",
#         "targsubtype2",
#         "targsubtype2_txt",
#         "targsubtype3",
#         "targsubtype3_txt",
#
#         "natlty1",
#         "natlty1_txt",
#         "natlty2",
#         "natlty2_txt",
#         "natlty3",
#         "natlty3_txt",
#
#         "gname",
#         "gname2",
#         "gname3",
#
#         "motive",
#         "nperps",
#
#         "weaptype1",
#         "weaptype1_txt",
#         "weapsubtype1",
#         "weapsubtype1_txt",
#         "weaptype2",
#         "weaptype2_txt",
#         "weapsubtype2",
#         "weapsubtype2_txt",
#         "weaptype3",
#         "weaptype3_txt",
#         "weapsubtype3",
#         "weapsubtype3_txt",
#         "weaptype4",
#         "weaptype4_txt",
#         "weapsubtype4",
#         "weapsubtype4_txt",
#
#         "nkill",
#         "nwound",
#     ]
#     return create_sub_table(flow_first_normalize(CSV_DATA_MAIN_TABLE), columns)
#
#
# @pytest.fixture(scope='module')
# def cities(clean_table):
#     return normalize_city_table(clean_table)
#
# @pytest.fixture(scope='module')
# def groups(clean_table):
#     return normalize_group_table(clean_table)
#
# @pytest.fixture(scope='module')
# def clean_table_with_city_ids(clean_table, cities):
#     return apply_city_id_on_main_csv(clean_table, cities)
#
#
#
#
# def test_normalize_region_table(clean_table):
#     result = normalize_region_table(clean_table)
#     print(result)
#     assert len(result.columns.tolist()) == 2
#
#
# def test_normalize_country_table(clean_table):
#     result = normalize_country_table(clean_table)
#     print(result)
#     assert len(result.columns.tolist()) == 3
#
#
# def test_normalize_data(clean_table):
#     result = normalize_city_table(clean_table)
#     print(result)
#     assert len(result.columns.tolist()) == 3
#
#
#
#
# def test_normalize_terror_location(clean_table_with_city_ids):
#     result = normalize_terror_location_table(clean_table_with_city_ids)
#     print(result)
#     assert len(result.columns.tolist()) == 5
#
# # def test_normalize_weapon_table(clean_table):
# #     result = normalize_weapon_table(clean_table)
# #     print(result.to_string(index=False))
# #     assert len(result.columns.tolist()) == 2
#
#
# def test_normalize_attack_type_table(clean_table):
#     result = normalize_attack_type_table(clean_table)
#     print(result.to_string(index=False))
#     assert len(result.columns.tolist()) == 2
#
#
# def test_normalize_target_type_table(clean_table):
#     result = normalize_target_type_table(clean_table)
#     print(result.to_string(index=False))
#     assert len(result.columns.tolist()) == 2
#
#
# def test_normalize_nationality_table(clean_table):
#     result = normalize_nationality_table(clean_table)
#     print(result.to_string(index=False))
#     assert len(result.columns.tolist()) == 2
#
# def test_normalize_group_table(clean_table):
#     result = normalize_group_table(clean_table)
#     print(result)
#     assert len(result.columns.tolist()) == 2
#
# def test_apply_city_id_on_main_csv(clean_table, cities):
#     result = apply_city_id_on_main_csv(clean_table, cities)
#     print(result)
#     assert "city_id" in result.columns.tolist()
#
# def test_apply_groups_id_on_main_csv(clean_table, groups):
#     result = apply_groups_id_on_main_csv(clean_table, groups)
#     print(result)
#     assert all(g_id in result.columns.tolist() for g_id in ["group1_id", "group2_id", "group3_id"])
