from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")


def get_lat_lon_from_address(location_dict: dict) -> dict:
    location = geolocator.geocode(location_dict["country"])
    if location is None:
        raise KeyError
    return {
        **location_dict,
        "latitude": location.latitude,
        "longitude": location.longitude
    }


if __name__ == '__main__':
    print(get_lat_lon_from_address("Canada"))
