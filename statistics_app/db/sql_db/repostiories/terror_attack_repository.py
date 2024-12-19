from typing import List

from data_management_app.db.sql_db.models import *
from statistics_app.db.sql_db.database import session_maker


def get_all_terror_attacks() -> List[TerrorAttack]:
    with session_maker() as session:
        return session.query(TerrorAttack).join(TerrorAttackTerrorLocation).join(TerrorLocation).all()