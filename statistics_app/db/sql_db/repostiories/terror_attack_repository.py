import pandas as pd
from statistics_app.db.sql_db.database import engine

import statistics_app.db.sql_db.repostiories.queries_terror_attack_repository as queries


# e_1
def get_deadliest_attack() -> pd.DataFrame:
    query = queries.query_get_deadliest_attack
    return pd.read_sql_query(query, engine)


# e_2
def get_average_casualties_query() -> pd.DataFrame:
    query = queries.query_get_average_casualties
    return pd.read_sql_query(query, engine).dropna(subset=["latitude", "longitude"])


# e_3
def get_top_5_groups_by_attacks_query() -> pd.DataFrame:
    query = queries.query_get_top_5_groups_by_attacks
    return pd.read_sql_query(query, engine).dropna(subset=['group'])


# e_6
def get_attack_change_percentage_by_region_query() -> pd.DataFrame:
    query = queries.query_get_attack_change_percentage_by_region
    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"]
    return df_filtered


# e_8
def get_most_active_groups_by_region_query() -> pd.DataFrame:
    query = queries.query_get_most_active_groups_by_region
    df = pd.read_sql_query(query, engine).dropna(subset=['group'])
    df_filtered = df[df['region'] != "Unknown"]
    return df_filtered


# e_11
def get_region_targets_intersection_query() -> pd.DataFrame:
    query = queries.query_get_region_targets_intersection
    df = pd.read_sql_query(query, engine).dropna(subset=['group'])
    df_filtered = df[df['region'] != "Unknown"]
    return df_filtered


# e_13
def get_groups_involved_in_same_attacks_query() -> pd.DataFrame:
    query = queries.query_get_groups_involved_in_same_attacks
    return pd.read_sql_query(query, engine)


# e_14
def get_shared_attack_strategies_by_region_query() -> pd.DataFrame:
    query = queries.query_get_shared_attack_strategies_by_region
    df = pd.read_sql_query(query, engine)
    df_filtered = df[df['region'] != "Unknown"].dropna(subset=['group']).dropna(subset=['attack_type'])
    return df_filtered


# e_16
def get_high_intergroup_activity_by_region_query() -> pd.DataFrame:
    query = queries.query_get_high_intergroup_activity_by_region
    return pd.read_sql_query(query, engine)


# e_19
def get_similar_goals_timeline_by_group_query() -> pd.DataFrame:
    query = queries.query_get_similar_goals_timeline_by_group
    return pd.read_sql_query(query, engine)


if __name__ == '__main__':
    pass
    print(get_similar_goals_timeline_by_group_query().columns.tolist())  # e19
    # print(get_high_intergroup_activity_by_region_query().columns.tolist()) # e16
    # print(get_shared_attack_strategies_by_region_query().columns.tolist()) # e14
    # print(get_groups_involved_in_same_attacks_query().columns.tolist()) # e13
    # print(get_region_targets_intersection_query().columns.tolist()) # e11
    # print(get_most_active_groups_by_region_query().columns.tolist()) # e8
    # print(get_attack_change_percentage_by_region_query()) # e6
    # print(get_top_5_groups_by_attacks_query()) # e3
    # print(get_average_casualties_query().columns.tolist()) # e2
    # print(get_deadliest_attack()) # e_1
