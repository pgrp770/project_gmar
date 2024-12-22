from typing import List, Dict
import pandas as pd
from sqlalchemy.sql import text
from data_management_app.db.sql_db.models import *
from statistics_app.db.sql_db.database import session_maker, engine
from collections import defaultdict

def get_all_terror_attacks() -> List[TerrorAttack]:
    with session_maker() as session:
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
        return session.query(TerrorAttack).all()

# def get_all_terror_attacks() -> List[Dict]:
#     query = '''
#         SELECT
#             ta.id AS terror_attack_id,
#             ta.date,
#             ta.kills,
#             ta.wounds,
#             ta.summary,
#             ta.terrorist_amount,
#             ta.terror_location_id,
#             tt.name AS target_type_name
#         FROM terror_attacks AS ta
#         LEFT JOIN terror_attack_target_type_relations AS tatt
#             ON ta.id = tatt.terror_attack_id
#         LEFT JOIN target_types AS tt
#             ON tatt.target_type_id = tt.id
#         LEFT JOIN terror_locations AS tl
#             ON ta.terror_location_id = tl.id
#     '''
#
#     df = pd.read_sql_query(query, engine)
#     grouped_df = df.groupby('terror_attack_id').agg(list).reset_index()
#     return grouped_df
if __name__ == '__main__':
    print(get_all_terror_attacks())