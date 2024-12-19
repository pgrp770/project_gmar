from pandas import DataFrame
import toolz as tz

from data_management_app.db.sql_db.database import init_db
from data_management_app.db.sql_db.models import Region, Country, City, TerrorLocation, AttackType, Weapon, TargetType, \
    Group, Nationality, TerrorAttack
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *
from data_management_app.utils.pandas_utils import *


def insert_region_table_to_postgres(df_region: DataFrame) -> None:
    df_region = pd.concat([df_region, pd.DataFrame({'region': [0], 'region_txt': ['Unknown']})], ignore_index=True)
    return t.pipe(
        df_region.dropna().drop_duplicates(subset=None, keep='first', inplace=False),
        lambda df: df.rename(columns={'region': 'id', 'region_txt': 'region_name'}, inplace=False),
        lambda df: df.to_dict(orient='records'),
        tz.partial(map, lambda x: Region(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_country_table_to_postgres(df_country: DataFrame) -> None:
    df = df_country.dropna().dropna().drop_duplicates(subset="country_txt", keep='first', inplace=False)
    df['id'] = range(1, len(df) + 1)
    return tz.pipe(
        df,
        lambda d: d.rename(columns={'region': 'region_id', 'country_txt': 'country_name'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Country(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


# apply_city_id_on_main_csv,
def insert_city_table_to_postgres(df_city: DataFrame) -> None:
    return tz.pipe(
        df_city.dropna().dropna().drop_duplicates(subset="city", keep='first', inplace=False),
        lambda d: d.rename(columns={'city': 'city_name', 'city_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: City(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_terror_location_to_postgres(df_terror_location: DataFrame) -> None:
    return tz.pipe(
        df_terror_location.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False),
        lambda d: d.rename(columns={'terror_location_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorLocation(**x)),
        list,
        lambda di: insert_many_generic(di),
    )


def insert_weapon(weapon_df:DataFrame) -> None:
    return tz.pipe(
        weapon_df,
        lambda d: d.rename(columns={'weapon_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Weapon(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
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

    return tz.pipe(
        terror_attack_df,
        lambda d: d.rename(columns={'Date':'date', 'nkill': 'kills', 'nwound': 'wounds', 'nperps':'terrorist_amount'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorAttack(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
def insertion_postgres_coutnry_region_cities_terror_location():
    df = main_flow_clean_csv()
    insert_region_table_to_postgres(normalize_region_table(df))

    insert_country_table_to_postgres(normalize_country_table(df))

    df_country = normalize_country_table(df).dropna().dropna().drop_duplicates(subset="country_txt", keep='first',                                                                   inplace=False)
    df_country['country_id'] = range(1, len(df_country) + 1)
    apply_country_id_on_main_csv(df, df_country)

    df_city = normalize_city_table(df).dropna().dropna().drop_duplicates(subset="city", keep='first', inplace=False)
    apply_city_id_on_main_csv(df, df_city)

    insert_city_table_to_postgres(normalize_city_table(df))

    a = normalize_terror_location_table(df)
    insert_terror_location_to_postgres(a)
    df_terror_location = a.dropna().dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',inplace=False)
    apply_terror_location_id_on_main_csv(df, df_terror_location)



if __name__ == '__main__':

    # insertion_postgres_coutnry_region_cities_terror_location()
    df = main_flow_clean_csv()
    # insert_attack_type(normalize_attack_type_table(df))
    # insert_weapon(normalize_weapon_table(df))
    # insert_target_type(normalize_target_type_table(df))
    # insert_group(normalize_group_table(df))
    # insert_nationality(normalize_nationality_table(df))
    insert_terror_attack(normalize_terror_attack_table(df))

