import math
from typing import List, Dict
import pandas as pd

from statistics_app.db.sql_db.repostiories.location_repository import *
from statistics_app.db.sql_db.repostiories.terror_attack_repository import get_all_terror_attacks, get_deadliest_attack, \
    get_average_casualties_query, get_top_5_groups_by_attacks_query, get_attack_change_percentage_by_region_query, \
    get_most_active_groups_by_region_query, get_region_targets_intersection_query, \
    get_groups_involved_in_same_attacks_query, get_shared_attack_strategies_by_region_query, \
    get_high_intergroup_activity_by_region_query, get_similar_goals_timeline_by_group_query

import statistics_app.services.routes_services.statistic_route_services.data_for_service as data_service


# 1
def get_deadliest_attack_endpoint_service(limit:int) -> List[Dict]:
    a = get_deadliest_attack()

    a_grouped = a.groupby('attack_type', as_index=False).agg({'casualties': 'sum'})

    a_sorted = a_grouped.sort_values(by='casualties', ascending=False)

    return a_sorted.head(limit).to_dict('records')



def first_nonzero(series):
    non_zero_values = series[series != 0]
    return non_zero_values.iloc[0] if not non_zero_values.empty else 0

# 2
def get_average_casualties(target: str, limit: int) -> List[Dict]:
    df = get_average_casualties_query()
    df = df.dropna(subset=["latitude", "longitude"])


    grouped = df.groupby(target).agg(
        casualties=("casualties", "sum"),
        latitude=("latitude", first_nonzero),
        longitude=("longitude", first_nonzero)
    ).reset_index()

    total_casualties = grouped["casualties"].sum()
    grouped["casualties_average"] = (grouped["casualties"] / total_casualties) * 100

    grouped = grouped.sort_values("casualties", ascending=False)
    grouped = grouped[grouped[target] != "Unknown"]
    grouped = grouped.head(limit) if limit > 0 else grouped

    return grouped.to_dict(orient="records")


# 3
def get_top_5_groups_by_attacks():

    df = get_top_5_groups_by_attacks_query()
    group_fatalities = df.groupby('group')['casualties'].sum().reset_index()
    sorted_groups = group_fatalities.sort_values(by='casualties', ascending=False)
    return sorted_groups.to_dict('records')

# 6
def get_attack_change_percentage_by_region(limit=0):
    df = get_attack_change_percentage_by_region_query()

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['year'] = df['year'].replace(2068, 1968)

    # Get first and last years for each region
    grouped = df.groupby('region').agg(
        first_year=('year', 'min'),
        last_year=('year', 'max'),
        latitude=('latitude', first_nonzero),
        longitude=('longitude', first_nonzero)

    ).reset_index()

    first_year_data = (
        df[df['year'] == df.groupby('region')['year'].transform('min')]
        .groupby('region')
        .agg(
            first_casualties=('casualties', 'sum'),
         )
        .reset_index()
    )

    last_year_data = (
        df[df['year'] == df.groupby('region')['year'].transform('max')]
        .groupby('region')
        .agg(last_casualties=('casualties', 'sum'))
        .reset_index()
    )

    # Merge the first and last year data with the grouped data
    grouped = grouped.merge(first_year_data, on='region').merge(last_year_data, on='region')

    # Calculate the attack change percentage
    grouped['attack_change_percentage'] = ((grouped['last_casualties'] - grouped['first_casualties']) / grouped[
        'first_casualties']) * 100

    # Select and return the relevant columns
    result = grouped[['region', 'latitude', 'longitude', 'first_year', 'last_year', 'attack_change_percentage']]
    result.replace()
    result.sort_values(by='attack_change_percentage', ascending=False)
    result['attack_change_percentage'] = result['attack_change_percentage'].replace(math.inf, 0)
    result = result.head(limit) if limit > 0 else result
    return result.to_dict('records')

# 8


def get_most_active_groups_by_region():
    df = get_most_active_groups_by_region_query()


    grouped = df.groupby('region').agg(
        group=('group', lambda x: x.mode()[0]),
        latitude=('latitude', first_nonzero),
        longitude=('longitude', first_nonzero),
        attack_count=('group', 'size')

    ).reset_index()
    return grouped.to_dict('records')


# 11
def get_region_targets_intersection(target):

    df = get_region_targets_intersection_query()
    print(df.columns.tolist())
    df_exploded = df.explode('group').explode('target_type')

    grouped = df_exploded.groupby([target, 'target_type']).agg(
        groups=('group', lambda x: list(set(x.dropna()))),
        latitude=('latitude', first_nonzero),
        longitude=('longitude', first_nonzero)
    ).reset_index()
    grouped_by_region = grouped.groupby(target).agg(
        target_type=('target_type', lambda x: list(set(x))),
        groups=('groups', lambda x: list(x)),
        latitude=('latitude', first_nonzero),
        longitude=('longitude', first_nonzero)
    ).reset_index()

    shared_targets = grouped_by_region[grouped_by_region['groups'].apply(len) > 1]

    return shared_targets.to_dict('records')

# 13
def get_groups_involved_in_same_attacks():
    df = get_groups_involved_in_same_attacks_query()
    df = df.dropna(subset=['groups'])
    df['groups'] = df['groups'].apply(lambda x: x.split(', ') if x else [])
    df_filtered = df[df['groups'].apply(len) > 1]
    return df_filtered.to_dict('records')


# 14
def get_shared_attack_strategies_by_region(target):
    df = get_shared_attack_strategies_by_region_query()

    df_exploded = df.explode('group').explode('attack_type')

    df_exploded.dropna(subset=['group', 'attack_type'], inplace=True)

    grouped = df_exploded.groupby(['region', 'attack_type']).agg(
        group=('group', lambda x: list(set(x))),
        latitude=('latitude', 'first'),
        longitude=('longitude', 'first')
    ).reset_index()

    grouped['group_count'] = grouped['group'].apply(len)

    max_groups = (
        grouped.groupby('region')
        .apply(lambda x: x.nlargest(1, 'group_count'))
        .reset_index(drop=True)
    )

    result = max_groups.to_dict(orient='records')

    return result

# 16
def get_high_intergroup_activity_by_region(target: str):
    df = get_high_intergroup_activity_by_region_query()

    # Group by the target ('region' or 'country') and calculate unique group counts
    group_count = df.groupby([target])['group'].nunique().reset_index()

    # Rename the columns to reflect the unique group count
    group_count.columns = [target, 'unique_group_count']

    # Add latitude and longitude by taking the first occurrence for each group
    lat_lon = df.groupby([target]).agg({'latitude':first_nonzero, 'longitude': first_nonzero}).reset_index()

    # Merge the latitude and longitude with the unique group count data
    result = pd.merge(group_count, lat_lon, on=target)

    # Return the result with the target, unique group count, latitude, and longitude
    return result.to_dict('records')


# 19
def get_similar_goals_timeline_by_group():
    df = get_similar_goals_timeline_by_group_query()

    df['date'] = pd.to_datetime(df['date'])

    df['year'] = df['date'].dt.year

    df.dropna(subset=['group'], inplace=True)

    df_cleaned = df[df['group'].apply(lambda x: len(x) > 0)]

    df_exploded = df_cleaned.explode('group').explode('target_type')

    grouped = (df_exploded.groupby(['year', 'target_type'])
               .agg(groups=('group', lambda x: list(set(x))))
               .reset_index())

    same_target_groups = grouped[grouped['groups'].apply(lambda x: len(x) > 1)]

    return same_target_groups.to_dict('records')



if __name__ == '__main__':
    pass
    print(get_similar_goals_timeline_by_group()) # 19
    # print(get_high_intergroup_activity_by_region("region")) # 16
    # print(get_shared_attack_strategies_by_region("region")) # 14
    # print(get_groups_involved_in_same_attacks()) # 13
    # print(get_region_targets_intersection("country")) # 11
    # print(get_most_active_groups_by_region()) # 8
    # print(get_attack_change_percentage_by_region(5))# 6
    # print(get_top_5_groups_by_attacks()) # 3
    # print(get_average_casualties("region", 5)) # 2
    # print(get_deadliest_attack_endpoint_service(5)) # 1
