from typing import List, Dict
import pandas as pd
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import text
from data_management_app.db.sql_db.models import *
from statistics_app.db.sql_db.database import session_maker, engine
from collections import defaultdict


# def get_all_terror_attacks() -> List[TerrorAttack]:
#     with session_maker() as session:
        #
        #     query = text('''
        #     SELECT ta.*, tt.*
        #     FROM terror_attacks AS ta
        #     LEFT JOIN terror_attack_target_type_relations AS tatt
        #         ON ta.id = tatt.terror_attack_id
        #     LEFT JOIN target_types AS tt
        #         ON tatt.target_type_id = tt.id
        #
        # ''')
        #     result = session.execute(query).fetchall()
        #     print(result)
        # return (session.query(TerrorAttack, TerrorAttackAttackType, AttackType)
        #         .join(TerrorAttack.attack_types)
        #         .join(TerrorAttackAttackType.attack_type)
        #         .all())
        # return (session.query(TerrorAttack)
        #         .options(joinedload((TerrorAttack.attack_types)))
        #         .join(TerrorAttackTargetType)
        #         .options(joinedload(TerrorAttackAttackType.attack_type))
        #         .all())

# e_1
def get_all_terror_attacks() -> List[Dict]:
    query = '''
        SELECT
            ta.id AS terror_attack_id,
            ta.date,
            ta.kills,
            ta.wounds,
            ta.summary,
            ta.terrorist_amount,
            ta.terror_location_id,
            tl.longitude,
            tl.latitude,
            city.name as city,
            country.name as country,
            region.name as region
        FROM terror_attacks AS ta
       
        LEFT JOIN terror_locations AS tl
            ON ta.terror_location_id = tl.id
        LEFT JOIN cities AS city
            ON tl.city_id = city.id
        LEFT JOIN countries AS country
            ON city.country_id = country.id
        LEFT JOIN regions AS region
            ON region.id = country.region_id
    '''

    df = pd.read_sql_query(query, engine)
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df

# e_1
def get_deadliest_attack() -> pd.DataFrame:

    query ='''
    

SELECT
    ta.id AS terror_attack_id,
    ta.date,
    ta.summary,
    ta.terrorist_amount,
    at.name AS attack_type,
    (ta.wounds + ta.kills * 2) AS casualties  -- Add this line to calculate casualties
    FROM terror_attacks AS ta
    LEFT JOIN terror_attack_attack_type_relations AS taat
        ON ta.id = taat.terror_attack_id
    LEFT JOIN attack_types AS at
        ON at.id = taat.attack_type_id
    '''

    df = pd.read_sql_query(query, engine)
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df

#e_2
def get_average_casualties_query() -> pd.DataFrame:

    query = '''
    SELECT
        ta.id AS terror_attack_id,
        ta.date,
        tl.longitude,
        tl.latitude,
        city.name AS city,
        country.name AS country,
        region.name AS region,
        (ta.wounds + ta.kills * 2) AS casualties -- Calculating casualties
    FROM terror_attacks AS ta
    LEFT JOIN terror_attack_attack_type_relations AS taat
        ON ta.id = taat.terror_attack_id
    LEFT JOIN terror_locations AS tl
        ON ta.terror_location_id = tl.id
    LEFT JOIN cities AS city
        ON tl.city_id = city.id
    LEFT JOIN countries AS country
        ON city.country_id = country.id
    LEFT JOIN regions AS region
        ON region.id = country.region_id
    '''

    df = pd.read_sql_query(query, engine)
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df

# e_3
def get_top_5_groups_by_attacks_query() -> pd.DataFrame:

    query = '''
    SELECT
        ta.id AS terror_attack_id,
        ta.date,
        (ta.wounds + ta.kills * 2) AS casualties,
        g.name as group
    FROM terror_attacks AS ta
    LEFT JOIN terror_attack_group_relations AS tag
        ON ta.id = tag.terror_attack_id
    LEFT JOIN groups AS g
        ON g.id = tag.group_id
    

    '''


    df = pd.read_sql_query(query, engine)
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df.dropna(subset=['group'])
# e_6
def get_attack_change_percentage_by_region_query() -> pd.DataFrame:


    query = '''
    SELECT
        ta.id AS terror_attack_id,
        ta.date,
        (ta.wounds + ta.kills * 2) AS casualties,
        tl.latitude,
        tl.longitude,
        region.name AS region
    FROM terror_attacks AS ta
    LEFT JOIN terror_locations AS tl
        ON ta.terror_location_id = tl.id
    LEFT JOIN cities AS city
        ON tl.city_id = city.id
    LEFT JOIN countries AS country
        ON city.country_id = country.id
    LEFT JOIN regions AS region
        ON region.id = country.region_id
    

    '''


    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"]
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df_filtered
# e_8
def get_most_active_groups_by_region_query() -> pd.DataFrame:


    query = '''
    SELECT
        ta.id AS terror_attack_id,
        ta.date,
        (ta.wounds + ta.kills * 2) AS casualties,
        tl.latitude,
        tl.longitude,
        region.name AS region,
        g.name AS group
    FROM terror_attacks AS ta
    LEFT JOIN terror_locations AS tl
        ON ta.terror_location_id = tl.id
    LEFT JOIN cities AS city
        ON tl.city_id = city.id
    LEFT JOIN countries AS country
        ON city.country_id = country.id
    LEFT JOIN regions AS region
        ON region.id = country.region_id
    LEFT JOIN terror_attack_group_relations AS tag
        ON ta.id = tag.terror_attack_id
    LEFT JOIN groups AS g
        ON g.id = tag.group_id
    LEFT JOIN terror_attack_target_type_relations AS taat
        ON ta.id = taat.terror_attack_id
    LEFT JOIN target_types AS at
        ON at.id = taat.target_type_id
    

    '''


    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"]
    return df_filtered.dropna(subset=['group'])


# e_11
def get_region_targets_intersection_query() -> pd.DataFrame:
    query = '''
    SELECT
    ta.id AS terror_attack_id,
    ta.date,
    (ta.wounds + ta.kills * 2) AS casualties,
    tl.latitude,
    tl.longitude,
    region.name AS region,
    country.name AS country,
    g.name AS group,
    tt.name AS target_type
FROM terror_attacks AS ta
LEFT JOIN terror_locations AS tl
    ON ta.terror_location_id = tl.id
LEFT JOIN cities AS city
    ON tl.city_id = city.id
LEFT JOIN countries AS country
    ON city.country_id = country.id
LEFT JOIN regions AS region
    ON region.id = country.region_id
LEFT JOIN terror_attack_group_relations AS tag
    ON ta.id = tag.terror_attack_id
LEFT JOIN groups AS g
    ON g.id = tag.group_id
LEFT JOIN terror_attack_target_type_relations AS tat
    ON ta.id = tat.terror_attack_id
LEFT JOIN target_types AS tt
    ON tt.id = tat.target_type_id;

    '''

    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"]
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df_filtered.dropna(subset=['group'])


# e_13
def get_groups_involved_in_same_attacks_query() -> pd.DataFrame:
    query = '''
        SELECT
            ta.id AS terror_attack_id,
            ta.date,
            (ta.wounds + ta.kills * 2) AS casualties,
            tl.latitude,
            tl.longitude,
            country.name AS country,
            STRING_AGG(g.name, ', ') AS groups
        FROM terror_attacks AS ta
        LEFT JOIN terror_locations AS tl
            ON ta.terror_location_id = tl.id
        LEFT JOIN cities AS city
            ON tl.city_id = city.id
        LEFT JOIN countries AS country
            ON city.country_id = country.id
        LEFT JOIN terror_attack_group_relations AS tag
            ON ta.id = tag.terror_attack_id
        LEFT JOIN groups AS g
            ON g.id = tag.group_id
        GROUP BY ta.id, ta.date, ta.wounds, ta.kills, tl.latitude, tl.longitude, country.name;


    '''

    return  pd.read_sql_query(query, engine)


# e_14
def get_shared_attack_strategies_by_region_query() -> pd.DataFrame:
    query = '''
    SELECT
    ta.id AS terror_attack_id,
    ta.date,
    (ta.wounds + ta.kills * 2) AS casualties,
    tl.latitude,
    tl.longitude,
    region.name AS region,
    country.name AS country,
    g.name AS group,
    tt.name AS attack_type
FROM terror_attacks AS ta
LEFT JOIN terror_locations AS tl
    ON ta.terror_location_id = tl.id
LEFT JOIN cities AS city
    ON tl.city_id = city.id
LEFT JOIN countries AS country
    ON city.country_id = country.id
LEFT JOIN regions AS region
    ON region.id = country.region_id
LEFT JOIN terror_attack_group_relations AS tag
    ON ta.id = tag.terror_attack_id
LEFT JOIN groups AS g
    ON g.id = tag.group_id
LEFT JOIN terror_attack_attack_type_relations AS tat
    ON ta.id = tat.terror_attack_id
LEFT JOIN attack_types AS tt
    ON tt.id = tat.attack_type_id;

    '''

    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"].dropna(subset=['group'])
    # grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
    return df_filtered.dropna(subset=['attack_type'])
# e_16
def get_high_intergroup_activity_by_region_query() -> pd.DataFrame:
    query = '''
    SELECT
    ta.id AS terror_attack_id,
    ta.date,
    (ta.wounds + ta.kills * 2) AS casualties,
    tl.latitude,
    tl.longitude,
    region.name AS region,
    country.name AS country,
    g.name AS group
    FROM terror_attacks AS ta
    LEFT JOIN terror_locations AS tl
        ON ta.terror_location_id = tl.id
    LEFT JOIN cities AS city
        ON tl.city_id = city.id
    LEFT JOIN countries AS country
        ON city.country_id = country.id
    LEFT JOIN regions AS region
        ON region.id = country.region_id
    LEFT JOIN terror_attack_group_relations AS tag
        ON ta.id = tag.terror_attack_id
    LEFT JOIN groups AS g
        ON g.id = tag.group_id


    '''


    return pd.read_sql_query(query, engine)
# e_19
def get_similar_goals_timeline_by_group_query() -> pd.DataFrame:
    query = '''
    SELECT
    ta.id AS terror_attack_id,
    ta.date,
    region.name AS region,
    country.name AS country,
    tt.name as target_type,
    g.name AS group
    FROM terror_attacks AS ta
    LEFT JOIN terror_locations AS tl
        ON ta.terror_location_id = tl.id
    LEFT JOIN cities AS city
        ON tl.city_id = city.id
    LEFT JOIN countries AS country
        ON city.country_id = country.id
    LEFT JOIN regions AS region
        ON region.id = country.region_id
    LEFT JOIN terror_attack_group_relations AS tag
        ON ta.id = tag.terror_attack_id
    LEFT JOIN groups AS g
        ON g.id = tag.group_id
    LEFT JOIN terror_attack_target_type_relations AS tat
        ON ta.id = tat.terror_attack_id
    LEFT JOIN target_types AS tt
        ON tt.id = tat.target_type_id;


    '''


    return pd.read_sql_query(query, engine)

if __name__ == '__main__':
    pass
    print(get_similar_goals_timeline_by_group_query().columns.tolist()) # e19
    # print(get_high_intergroup_activity_by_region_query().columns.tolist()) # e16
    # print(get_shared_attack_strategies_by_region_query().columns.tolist()) # e14
    # print(get_groups_involved_in_same_attacks_query().columns.tolist()) # e13
    # print(get_region_targets_intersection_query().columns.tolist()) # e11
    # print(get_most_active_groups_by_region_query().columns.tolist()) # e8
    # print(get_attack_change_percentage_by_region_query()) # e6
    # print(get_top_5_groups_by_attacks_query()) # e3
    # print(get_average_casualties_query().columns.tolist()) # e2
    # print(get_deadliest_attack()) # e_1
