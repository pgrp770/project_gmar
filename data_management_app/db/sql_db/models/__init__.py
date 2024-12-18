from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .region import Region
from .country import Country
from .city import City
from .terror_location import TerrorLocation

from .nationality import Nationality
from .terror_attack import TerrorAttack
from .terror_attack_nationality import TerrorAttackNationality

from .group import Group
from .terror_attack_group import TerrorAttackGroup

from .target_type import TargetType
from .terror_attack_target_type import TerrorAttackTargetType

from .attack_type import AttackType
from .terror_attack_attack_type import TerrorAttackAttackType


from .weapon import Weapon
from .terror_attack_weapon import TerrorAttackWeapon

from .terror_attack_terror_location import TerrorAttackTerrorLocation