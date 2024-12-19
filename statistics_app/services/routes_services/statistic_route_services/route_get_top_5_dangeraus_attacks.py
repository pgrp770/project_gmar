from dataclasses import asdict
from typing import List
import pandas as pd
from statistics_app.db.sql_db.repostiories.terror_attack_repository import get_all_terror_attacks
import toolz as tz



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


if __name__ == '__main__':
    print(get_amount_terror_attacks_by_region("df"))
    # print(calculate_percentage_change_e8())
    # 3 print(top_5_groups_fatals(foo()))
    # 2 print(average_fatal_by_country(get_attacks_order_by_fatal()))
    # 1 print(get_attacks_order_by_fatal())