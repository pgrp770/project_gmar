from dataclasses import asdict
from itertools import combinations
from typing import List
import pandas as pd
from statistics_app.db.sql_db.repostiories.terror_attack_repository import get_all_terror_attacks
import toolz as tz
import numpy as np



# 1
def get_attacks_order_by_fatal():
    attacks = get_all_terror_attacks()
    return tz.pipe([
        {
            "id": attack.id,
            "date": attack.date,
            "fatal": attack.kills + attack.wounds,
            "country": attack.terror_location.city.country.name,
            "region": attack.terror_location.city.country.region.name,
        }
        for attack in attacks
    ],
        lambda x : sorted(x, key=lambda y: y["fatal"], reverse=True),
    )

def get_top_5_dangeraus_attacks(li: List[dict]):
    return li[:5]


# 2
def average_fatal_by_region(li: List[dict]):
    return tz.pipe(
        li,
        lambda x: tz.groupby(lambda item: item['region'], x),
        lambda grouped: {region: len(items) for region, items in grouped.items()}
    )

def average_fatal_by_country(li: List[dict]):
    return tz.pipe(
        li,
        lambda x: tz.groupby(lambda item: item['country'], x),
        lambda grouped: {region: len(items) for region, items in grouped.items()}
    )

# 3
def foo():
    attacks = get_all_terror_attacks()
    return tz.pipe([
        {
            "id": attack.id,
            "date": attack.date,
            "fatal": attack.kills + attack.wounds,
            "country": attack.terror_location.city.country.name,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups]
        }
        for attack in attacks
    ],
        lambda x : sorted(x, key=lambda y: y["fatal"], reverse=True),
    )


def top_5_groups_fatals(li: List[dict]):
    df = pd.DataFrame(li)
    expanded_df = df.explode('groups')
    group_fatalities = expanded_df.groupby('groups')['fatal'].sum().reset_index()
    sorted_groups = group_fatalities.sort_values(by='fatal', ascending=False)
    return sorted_groups.to_dict('records')



def calculate_percentage_change_e8():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)
    df['year'] = pd.to_datetime(df['date']).dt.year
    yearly_data = df.groupby(['region', 'year']).size().reset_index(name='attack_count')
    result = yearly_data.groupby('region').apply(
        lambda group: {
            group['region'].iloc[0]:float(  # More informative key
                (group['attack_count'].iloc[-1] - group['attack_count'].iloc[0]) / group['attack_count'].iloc[0] * 100)
        }
    ).reset_index(drop=True)
    return result.tolist()

# e8
def get_amount_terror_attacks_by_region():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)

    # הרחבת קבוצות הטרור כך שכל שורה תייצג קשר בין קבוצה לאזור
    df_exploded = df.explode('groups')

    # חישוב כמות ההתקפות לפי אזור וקבוצה
    grouped = df_exploded.groupby(['region', 'groups']).size().reset_index(name='attack_count')
    most_active_groups = grouped.loc[grouped.groupby('region')['attack_count'].idxmax()]

    return most_active_groups.to_dict('records')

# 11
def corrolation_between_regions_and_targets():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
            "targets": [target.target_type.name for target in attack.target_types]
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)
    df_exploded = df.explode('groups').explode('targets')

    grouped = df_exploded.groupby(['region', 'targets'])['groups'].apply(lambda x: list(set(x.dropna()))).reset_index()

    shared_targets = grouped[grouped['groups'].apply(len) > 1]

    return shared_targets.to_dict('records')

# 13
def friedns_group():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attacks
    ]

    df = pd.DataFrame(attacks_list)
    df['group_combinations'] = df['groups'].apply(
        lambda groups: list(combinations(groups, 2)) if len(groups) > 1 else None
    )

    df_exploded = df.explode('group_combinations').dropna(subset=['group_combinations'])

    collaborations = df_exploded.groupby('group_combinations').size().reset_index(name='attack_count')
    return collaborations.to_dict('records')
# 14
def get_connection_group_attack_type():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
            "attack_types": [attack.attack_type.name for attack in attack.attack_types]
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)

    df_exploded = df.explode('groups').explode('attack_types')
    df_exploded.dropna(subset="groups", inplace=True)

    grouped = df_exploded.groupby(['region', 'attack_types'])['groups'].apply(lambda x: list(set(x))).reset_index()

    shared_attack_types = grouped[grouped['groups'].apply(len) > 1]

    return shared_attack_types

# 16
def get_unique_groups_of_all_region():
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)
    df_exploded = df.explode('groups')

    # Filter out empty or NaN groups
    df_exploded = df_exploded.dropna(subset=['groups'])

    # Count the unique groups per region
    unique_groups_per_region = df_exploded.groupby('region')['groups'].nunique()

    # Display the result
    return unique_groups_per_region.to_dict()

# 19
def e19(year):
    attacks = get_all_terror_attacks()
    attacks_list = [
        {
            "id": attack.id,
            "date": attack.date,
            "region": attack.terror_location.city.country.region.name,
            "groups": [group.group.name for group in attack.groups],
            "target_types": [attack.target_type.name for attack in attack.target_types]
        }
        for attack in attacks
    ]
    df = pd.DataFrame(attacks_list)


    # Extract year from date
    df['year'] = df['date'].dt.year
    df.dropna(subset='groups', inplace=True)
    df_cleaned = df[df['groups'].apply(lambda x: len(x) > 0)]
    print(df_cleaned["groups"])
    # Explode the groups and target_types
    df_exploded = df_cleaned.explode('groups').explode('target_types')

    # Group by year and target_types, and aggregate the groups
    grouped = (df_exploded.groupby(['year', 'target_types'])
               .agg(groups=('groups', lambda x: list(set(x))))  # Unique groups
               .reset_index())

    # Filter rows with multiple groups sharing the same target in the same year
    same_target_groups = grouped[grouped['groups'].apply(lambda x: len(x) > 1)]

    print(same_target_groups.to_dict('records'))
if __name__ == '__main__':
    pass
    # 19 print(e19(1))
    # 16 print(get_unique_groups_of_all_region())
    # 14 print(get_connection_group_attack_type())
    # 13 print(friedns_group())
    # 11 print(corrolation_between_regions_and_targets())
    # 8 print(get_amount_terror_attacks_by_region("df"))
    # 6 print(calculate_percentage_change_e8())
    # 3 print(top_5_groups_fatals(foo()))
    # 2 print(average_fatal_by_country(get_attacks_order_by_fatal()))
    # 1 print(get_attacks_order_by_fatal())