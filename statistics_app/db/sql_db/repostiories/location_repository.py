from sqlalchemy import func

from data_management_app.db.sql_db.database import session_maker
from data_management_app.db.sql_db.models import TerrorLocation, City, Country, Region


def get_coordinates_from_country(country_id: int):
    with session_maker() as session:
        city_coordinates = (
            session.query(
                TerrorLocation.latitude,
                TerrorLocation.longitude
            )
            .join(City, City.id == TerrorLocation.city_id)
            .join(Country, Country.id == City.country_id)
            .filter(Country.id == country_id)
            .first()
        )

        if city_coordinates:
            return {"latitude": city_coordinates[0], "longitude": city_coordinates[1]}
        else:
            return {"latitude": None, "longitude": None}



def get_coordinates_from_region(region_id: int):
    with session_maker() as session:
        city_coordinates = (
            session.query(
                TerrorLocation.latitude,
                TerrorLocation.longitude
            )
            .join(City, City.id == TerrorLocation.city_id)
            .join(Country, Country.id == City.country_id)
            .join(Region, Region.id == Country.region_id)
            .filter(Region.id == region_id)
            .first()
        )
        return {
            "latitude": city_coordinates[0] if city_coordinates else None,
            "longitude": city_coordinates[1] if city_coordinates else None
        }