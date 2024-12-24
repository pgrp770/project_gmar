from data_management_app.db.sql_db.database import init_db
from data_management_app.db.sql_db.models import *
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import *
from data_management_app.utils.pandas_utils import *
from pandas import DataFrame


def prepare_region_list_to_insert(df_region: DataFrame) -> List[dict]:
    return tz.pipe(
        df_region,
        lambda df: df.rename(columns={'region': 'id', 'region_txt': 'name'}, inplace=False),
        lambda df: df.to_dict(orient='records'),
        tz.partial(map, lambda x: Region(**x)),
        list
    )


def insert_country_table_to_postgres(df_country: DataFrame) -> DataFrame:
    tz.pipe(
        df_country.copy(),
        lambda df: df.rename(columns={'region': 'region_id', 'country_txt': 'name'}, inplace=False),
        lambda df: df.to_dict(orient='records'),
        tz.partial(map, lambda x: Country(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
    return df_country.rename(columns={'id': 'country_id'})


def insert_city_table_to_postgres(df_city: DataFrame) -> DataFrame:
    tz.pipe(
        df_city.copy(),
        lambda d: d.rename(columns={'city': 'name', 'city_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: City(**x)),
        list,
        lambda di: insert_many_generic(di),
    )
    return df_city


def insert_terror_location_to_postgres(df_terror_location: DataFrame) -> List[Dict]:
    return tz.pipe(
        df_terror_location.dropna().drop_duplicates(subset=["city_id", "longitude", "latitude"], keep='first',
                                                    inplace=False),
        lambda d: d.rename(columns={'terror_location_id': 'id'}, inplace=False), lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorLocation(**x)),
        list
    )


def insert_target_type(target_type_df: DataFrame) -> List[Dict]:
    return tz.pipe(
        target_type_df,
        lambda d: d.rename(columns={'target_type_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TargetType(**x)),
        list
    )


def insert_group(attack_df: DataFrame) -> List[Dict]:
    return tz.pipe(
        attack_df,
        lambda d: d.rename(columns={'group_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Group(**x)),
        list
    )


def insert_nationality(attack_df: DataFrame) -> List[Dict]:
    return tz.pipe(
        attack_df,
        lambda d: d.rename(columns={'nationality_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: Nationality(**x)),
        list
    )


def insert_attack_type(attack_type_df: DataFrame) -> List[Dict]:
    return tz.pipe(
        attack_type_df,
        lambda d: d.rename(columns={'attack_type_id': 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: AttackType(**x)),
        list
    )


def insert_terror_attack(terror_attack_df: DataFrame) -> List[Dict]:
    terror_attack_df.fillna({"terror_location_id": 0})
    terror_attack_df['terror_location_id'] = terror_attack_df['terror_location_id'].astype(int)
    return tz.pipe(
        terror_attack_df,
        lambda d: d.rename(columns={'Date': 'date', 'nkill': 'kills', 'nwound': 'wounds', 'nperps': 'terrorist_amount',
                                    "terror_attack_id": 'id'}, inplace=False),
        lambda d: d.to_dict(orient='records'),
        tz.partial(map, lambda x: TerrorAttack(**x)),
        list
    )


def main_flow_insert_tables():
    init_db()
    df = main_flow_clean_csv()
    insert_many_generic(prepare_region_list_to_insert(normalize_region_table(df)))
    df_country = insert_country_table_to_postgres(normalize_country_table(df))
    apply_country_id_on_main_csv(df, df_country)
    df_city = insert_city_table_to_postgres(normalize_city_table(df))
    apply_city_id_on_main_csv(df, df_city)
    terror_locations = normalize_terror_location_table(df)
    insert_many_generic(insert_terror_location_to_postgres(terror_locations))
    apply_terror_location_id_on_main_csv(df, terror_locations)
    insert_many_generic(insert_attack_type(normalize_attack_type_table(df)))
    insert_many_generic(insert_target_type(normalize_target_type_table(df)))
    insert_many_generic(insert_group(normalize_group_table(df)))
    insert_many_generic(insert_nationality(normalize_nationality_table(df)))
    insert_many_generic(insert_terror_attack(normalize_terror_attack_table(df)))
    # create_summery(
    #     from_list_to_actions(
    #         normalize_terror_attack_table(df)[['terror_attack_id', 'summary', 'Date']]
    #         .dropna()
    #         .assign(type='history')
    #         .to_dict('records')
    #     )
    # )
    # print("insert summery to elastic")
