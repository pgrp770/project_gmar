import math
from typing import List, Dict
from statistics_app.db.sql_db.repostiories.terror_attack_repository import *


def first_nonzero(series):
    non_zero_values = series[series != 0]
    return non_zero_values.iloc[0] if not non_zero_values.empty else 0


# 1
def get_deadliest_attack_endpoint_service(limit: int) -> List[Dict]:
    df = get_deadliest_attack()
    df_grouped = df.groupby('attack_type', as_index=False).agg({'casualties': 'sum'})
    df_sorted = df_grouped.sort_values(by='casualties', ascending=False)
    return df_sorted.head(limit).to_dict('records')


# 2
def get_average_casualties(target: str, limit: int) -> List[Dict]:
    df = get_average_casualties_query()
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
    grouped = grouped.merge(first_year_data, on='region').merge(last_year_data, on='region')
    grouped['attack_change_percentage'] = ((grouped['last_casualties'] - grouped['first_casualties']) / grouped[
        'first_casualties']) * 100
    result = grouped[['region', 'latitude', 'longitude', 'first_year', 'last_year', 'attack_change_percentage']]
    result.replace()
    result.sort_values(by='attack_change_percentage', ascending=False)
    result['attack_change_percentage'] = result['attack_change_percentage'].replace(math.inf, 0)
    result = result.head(limit) if limit > 0 else result
    return result.to_dict('records')


# 8
def get_most_active_groups_by_region():
    df = get_most_active_groups_by_region_query()
    group_count = df.groupby(['region', 'group']).size().reset_index(name='count')
    grouped_by_region = group_count.groupby('region').apply(
        lambda x: x.sort_values(by='count', ascending=False).head(5)[['group', 'count']].to_dict('records')
    ).reset_index(name='top_5_groups')
    lat_lon = df.groupby('region').agg(
        latitude=('latitude', 'first'),
        longitude=('longitude', 'first')
    ).reset_index()
    result = pd.merge(grouped_by_region, lat_lon, on='region', how='left')
    return result.to_dict('records')


# 11
def get_region_targets_intersection(target):
    df = get_region_targets_intersection_query()
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
    grouped = df_exploded.groupby([target, 'attack_type']).agg(
        group=('group', lambda x: list(set(x))),
        latitude=('latitude', 'first'),
        longitude=('longitude', 'first')
    ).reset_index()
    grouped['group_count'] = grouped['group'].apply(len)
    max_groups = (
        grouped.groupby(target)
        .apply(lambda x: x.nlargest(1, 'group_count'))
        .reset_index(drop=True)
    )
    result = max_groups.to_dict(orient='records')
    return result


# 16
def get_high_intergroup_activity_by_region(target: str):
    df = get_high_intergroup_activity_by_region_query()
    group_count = df.groupby([target])['group'].nunique().reset_index()
    group_count.columns = [target, 'unique_group_count']
    lat_lon = df.groupby([target]).agg({'latitude': first_nonzero, 'longitude': first_nonzero}).reset_index()
    result = pd.merge(group_count, lat_lon, on=target)
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
    # print(get_similar_goals_timeline_by_group()) # 19
    # print(get_high_intergroup_activity_by_region("region")) # 16
    # print(get_shared_attack_strategies_by_region("country")) # 14
    # print(get_groups_involved_in_same_attacks()) # 13
    # print(get_region_targets_intersection("country")) # 11
    # print(get_most_active_groups_by_region())  # 8
    # print(get_attack_change_percentage_by_region(5))# 6
    # print(get_top_5_groups_by_attacks()) # 3
    # print(get_average_casualties("region", 5)) # 2
    # print(get_deadliest_attack_endpoint_service(5)) # 1
