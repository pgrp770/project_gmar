from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .region import Region
from .country import Country
from .city import City
from .terror_location import TerrorLocation