# e_1
query_get_deadliest_attack = '''
    SELECT
        ta.id AS terror_attack_id,
        ta.date,
        ta.terrorist_amount,
        at.name AS attack_type,
        (ta.wounds + ta.kills * 2) AS casualties
    FROM terror_attacks AS ta
    LEFT JOIN terror_attack_attack_type_relations AS taat
        ON ta.id = taat.terror_attack_id
    LEFT JOIN attack_types AS at
        ON at.id = taat.attack_type_id
    '''


# e_2
query_get_average_casualties = '''
    SELECT
        ta.id AS terror_attack_id,
        tl.longitude,
        tl.latitude,
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


# e_3
query_get_top_5_groups_by_attacks = '''
    SELECT
        ta.id AS terror_attack_id,
        (ta.wounds + ta.kills * 2) AS casualties,
        g.name as group
    FROM terror_attacks AS ta
    LEFT JOIN terror_attack_group_relations AS tag
        ON ta.id = tag.terror_attack_id
    LEFT JOIN groups AS g
        ON g.id = tag.group_id
    '''

# e_6
query_get_attack_change_percentage_by_region = '''
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


# e_8
query_get_most_active_groups_by_region = '''
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


# e_11
query_get_region_targets_intersection = '''
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


# e_13
query_get_groups_involved_in_same_attacks = '''
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


# e_14
query_get_shared_attack_strategies_by_region = '''
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


# e_16
query_get_high_intergroup_activity_by_region = '''
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


# e_19
query_get_similar_goals_timeline_by_group = '''
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
