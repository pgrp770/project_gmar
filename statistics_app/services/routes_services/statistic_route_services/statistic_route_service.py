from itertools import combinations
from typing import List, Dict
import pandas as pd

from statistics_app.db.sql_db.repostiories.location_repository import *
from statistics_app.db.sql_db.repostiories.terror_attack_repository import get_all_terror_attacks
import toolz as tz

import statistics_app.services.routes_services.statistic_route_services.data_for_service as data_service


# 1
def get_deadliest_attack_endpoint_service(limit:int) -> List[Dict]:
    return tz.pipe(
        data_service.get_id_date_casualties_country_region(get_all_terror_attacks()),
        lambda x: sorted(x, key=lambda y: y["casualties"], reverse=True),
        lambda li: tz.take(limit, li) if limit > 0 else li,
        list
    )


# 2


def get_average_casualties(target: str, limit: int) -> List[Dict]:
    df = pd.DataFrame(data_service.get_id_date_casualties_country_region(get_all_terror_attacks()))

    grouped = df.groupby(target).agg(casualties=("casualties", "sum")).reset_index()

    total_casualties = grouped["casualties"].sum()
    grouped["casualties_average"] = (grouped["casualties"] / total_casualties) * 100

    grouped = grouped.sort_values("casualties", ascending=False)
    grouped = grouped.head(limit) if limit > 0 else grouped

    if target == "country":
        grouped['latitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['latitude'])
        grouped['longitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['longitude'])
    elif target == "region":
        grouped['latitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['latitude'])
        grouped['longitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['longitude'])

    return grouped.to_dict(orient="records")


# 3
def get_top_5_groups_by_attacks():

    df = pd.DataFrame(data_service.get_id_date_fatal_groups(get_all_terror_attacks()))
    expanded_df = df.explode('groups')
    group_fatalities = expanded_df.groupby('groups')['casualties'].sum().reset_index()
    sorted_groups = group_fatalities.sort_values(by='casualties', ascending=False)

    return sorted_groups.to_dict('records')

# 6
def get_attack_change_percentage_by_region():
    # Create DataFrame from raw data
    df = pd.DataFrame(data_service.get_id_date_region(get_all_terror_attacks()))

    # Add year column
    df['year'] = pd.to_datetime(df['date']).dt.year

    # Group by region and year, then count attacks
    yearly_data = df.groupby(['region', 'year']).size().reset_index(name='attack_count')

    # Add latitude and longitude
    yearly_data['latitude'] = yearly_data['region'].apply(lambda x: get_coordinates_from_region(x)['latitude'])
    yearly_data['longitude'] = yearly_data['region'].apply(lambda x: get_coordinates_from_region(x)['longitude'])

    # Calculate attack change percentage by region
    result = yearly_data.groupby('region').apply(
        lambda group: {
            'region': int(group['region'].iloc[0]),  # Explicitly convert to int
            'latitude': float(group['latitude'].iloc[0]),  # Explicitly convert to float
            'longitude': float(group['longitude'].iloc[0]),  # Explicitly convert to float
            'attack_change_percentage': float(
                (group['attack_count'].iloc[-1] - group['attack_count'].iloc[0]) / group['attack_count'].iloc[0] * 100)
        }
    ).tolist()  # Convert result to a list of dictionaries

    return result


# 8
def get_most_active_groups_by_region():

    df = pd.DataFrame(data_service.get_id_date_region_groups(get_all_terror_attacks()))
    df_exploded = df.explode('groups')
    grouped = df_exploded.groupby(['region', 'groups']).size().reset_index(name='attack_count')
    most_active_groups = grouped.loc[grouped.groupby('region')['attack_count'].idxmax()]

    return most_active_groups.to_dict('records')


# 11
def get_region_targets_intersection(target):

    df = pd.DataFrame(data_service.get_id_date_country_region_groups_targets(get_all_terror_attacks()))
    df_exploded = df.explode('groups').explode('targets')
    grouped = df_exploded.groupby([target, 'targets'])['groups'].apply(lambda x: list(set(x.dropna()))).reset_index()
    if target == "country":
        grouped['latitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['latitude'])
        grouped['longitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['longitude'])
    elif target == "region":
        grouped['latitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['latitude'])
        grouped['longitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['longitude'])

    shared_targets = grouped[grouped['groups'].apply(len) > 1]


    return shared_targets.to_dict('records')


# 13
def get_groups_involved_in_same_attacks():

    df = pd.DataFrame(data_service.get_id_groups(get_all_terror_attacks()))
    df['group_combinations'] = df['groups'].apply(lambda groups: list(combinations(groups, 2)) if len(groups) > 1 else None)
    df_exploded = df.explode('group_combinations').dropna(subset=['group_combinations'])
    collaborations = df_exploded.groupby('group_combinations').size().reset_index(name='attack_count')

    return collaborations.to_dict('records')


# 14
def get_shared_attack_strategies_by_region(target):

    df = pd.DataFrame(data_service.get_id_date_country_region_groups_attack_types(get_all_terror_attacks()))
    df_exploded = df.explode('groups').explode('attack_types')
    df_exploded.dropna(subset="groups", inplace=True)
    grouped = df_exploded.groupby([target, 'attack_types'])['groups'].apply(lambda x: list(set(x))).reset_index()
    if target == "country":
        grouped['latitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['latitude'])
        grouped['longitude'] = grouped['country'].apply(lambda x: get_coordinates_from_country(x)['longitude'])
    elif target == "region":
        grouped['latitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['latitude'])
        grouped['longitude'] = grouped['region'].apply(lambda x: get_coordinates_from_region(x)['longitude'])
    shared_attack_types = grouped[grouped['groups'].apply(len) > 1]


    return shared_attack_types.to_dict('records')


# 16
def get_high_intergroup_activity_by_region(target: str):

    df = pd.DataFrame(data_service.get_id_country_region_groups(get_all_terror_attacks()))
    df_exploded = df.explode('groups')
    df_exploded = df_exploded.dropna(subset=['groups'])
    unique_groups_per_region = df_exploded.groupby(target)['groups'].nunique()

    return unique_groups_per_region.to_dict()


# 19
def get_similar_goals_timeline_by_group():
    df = pd.DataFrame(data_service.get_id_date_region_groups_target_types(get_all_terror_attacks()))

    df['year'] = df['date'].dt.year
    df.dropna(subset='groups', inplace=True)
    df_cleaned = df[df['groups'].apply(lambda x: len(x) > 0)]
    df_exploded = df_cleaned.explode('groups').explode('target_types')

    grouped = (df_exploded.groupby(['year', 'target_types'])
               .agg(groups=('groups', lambda x: list(set(x))))  # Unique groups
               .reset_index())
    same_target_groups = grouped[grouped['groups'].apply(lambda x: len(x) > 1)]

    return same_target_groups.to_dict('records')


if __name__ == '__main__':
    pass
    # print(get_similar_goals_timeline_by_group())
    # print(get_high_intergroup_activity_by_region("country")) # 16
    print(get_shared_attack_strategies_by_region("region")) # 14
    # print(get_groups_involved_in_same_attacks()) # 13
    # print(get_region_targets_intersection("country")) # 11
    # print(get_most_active_groups_by_region()) # 8
    # print(get_attack_change_percentage_by_region())# 6
    # 3 print(get_top_5_groups_by_attacks())
    # print(get_average_casualties("country", 10))
    # 1 print(get_attacks_order_by_fatal())
