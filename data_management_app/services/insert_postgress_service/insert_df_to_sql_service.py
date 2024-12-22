from pandas import DataFrame
import toolz as tz

from data_management_app.db.elastic_db.repositories.summery_repository import create_summery
from data_management_app.db.sql_db.database import init_db
from data_management_app.db.sql_db.models import Region, Country, City, TerrorLocation, AttackType, Weapon, TargetType, \
    Group, Nationality, TerrorAttack
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
from data_management_app.services.insert_elastic_service.insert_summery_service import from_list_to_actions
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *
from data_management_app.utils.pandas_utils import *


def insert_region_table_to_postgres(df_region: DataFrame) -> None:
    df_region = pd.concat([df_region, pd.DataFrame({'region': [0], 'region_txt': ['Unknown']})], ignore_index=True)
    return t.pipe(
        df_region.dropna().drop_duplicates(subset=None, keep='first', inplace=False),
        lambda df: df.rename(columns={'region': 'id', 'region_txt': 'name'}, inplace=False),
        lambda df: df.to_dict(orient='records'),
        tz.partial(map, lambda x: Region(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_country_table_to_postgres(df_country: DataFrame) -> DataFrame:
    df = df_country.dropna().dropna().drop_duplicates(subset="country_txt", keep='first', inplace=False)
    df['id'] = range(1, len(df) + 1)
    tz.pipe(
        df.copy(),
        lambda d: d.rename(columns={'region': 'region_id', 'country_txt': 'name'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Country(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
    return df.rename(columns={'id': 'country_id'})


# apply_city_id_on_main_csv,
def insert_city_table_to_postgres(df_city: DataFrame) -> DataFrame:
    df = df_city.dropna().dropna().drop_duplicates(subset="city", keep='first', inplace=False)
    tz.pipe(
        df.copy(),
        lambda d: d.rename(columns={'city': 'name', 'city_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: City(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
    return df


def insert_terror_location_to_postgres(df_terror_location: DataFrame) -> None:
    return tz.pipe(
        df_terror_location.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False),lambda d: d.rename(columns={'terror_location_id': 'id'}, inplace=False),lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorLocation(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


# def insert_weapon(weapon_df:DataFrame) -> None:
#     return tz.pipe(
#         weapon_df,
#         lambda d: d.rename(columns={'weapon_id': 'id'}, inplace=False),
#         lambda d: d.to_dict(orient='records'),
#         tz.partial(map, lambda x: Weapon(**x)),
#         list,
#         lambda di: insert_many_generic(di),
#     )
def insert_target_type(target_type_df:DataFrame) -> None:
    return tz.pipe(
        target_type_df,
        lambda d: d.rename(columns={'target_type_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TargetType(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
def insert_group(attack_df:DataFrame) -> None:
    return tz.pipe(
        attack_df,
        lambda d: d.rename(columns={'group_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Group(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
def insert_nationality(attack_df:DataFrame) -> None:
    return tz.pipe(
        attack_df,
        lambda d: d.rename(columns={'nationality_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Nationality(**x)),
        list,
        lambda di: insert_many_generic(di),
    )

def insert_attack_type(attack_type_df:DataFrame) -> None:
    return tz.pipe(
        attack_type_df,
        lambda d: d.rename(columns={'attack_type_id':'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: AttackType(**x)),
        list,
        lambda di: insert_many_generic(di),
    )

def insert_terror_attack(terror_attack_df:DataFrame) -> None:
    terror_attack_df.fillna({"terror_location_id":0})
    terror_attack_df['terror_location_id'] = terror_attack_df['terror_location_id'].astype(int)
    return tz.pipe(
        terror_attack_df,
        lambda d: d.rename(columns={'Date':'date', 'nkill': 'kills', 'nwound': 'wounds', 'nperps':'terrorist_amount', "terror_attack_id": 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorAttack(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
def insertion_postgres_country_region_cities_terror_location():
    df = main_flow_clean_csv()
    insert_region_table_to_postgres(normalize_region_table(df))
    print("insert region table")
    df_country = insert_country_table_to_postgres(normalize_country_table(df))
    print("insert country table")
    apply_country_id_on_main_csv(df, df_country)
    df_city = insert_city_table_to_postgres(normalize_city_table(df))
    print("insert city table")
    apply_city_id_on_main_csv(df, df_city)
    df["city_id"] = df["city_id"].fillna(3).astype(int)
    terror_locations = normalize_terror_location_table(df)
    insert_terror_location_to_postgres(terror_locations)
    print("insert terror_locations table")
    df_terror_location = terror_locations.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False)
    apply_terror_location_id_on_main_csv(df, df_terror_location)
    return df



if __name__ == '__main__':
    init_db()

    df = insertion_postgres_country_region_cities_terror_location()
    insert_attack_type(normalize_attack_type_table(df))
    print("insert attack_type table")
    # insert_weapon(normalize_weapon_table(df))
    insert_target_type(normalize_target_type_table(df))
    print("insert target_type table")
    insert_group(normalize_group_table(df))
    print("insert group table")
    insert_nationality(normalize_nationality_table(df))
    print("insert nationality table")
    insert_terror_attack(normalize_terror_attack_table(df))
    print("insert terror_attack table")
    # create_summery(
    #     from_list_to_actions(
    #         normalize_terror_attack_table(df)[['terror_attack_id', 'summary', 'Date']]
    #         .dropna()
    #         .assign(type='history')
    #         .to_dict('records')
    #     )
    # )
    # print("insert summery to elastic")
