def validate_groq_json(groq_json: dict) -> dict:
    return {
        "category": groq_json["category"],
        "country": groq_json["country"],
        "region": groq_json["continent"],
        "latitude": groq_json["country_latitude"],
        "longitude": groq_json["country_longitude"],
    }
def validate_keys(di: dict):
    list_keys = ['category', 'country', 'longitude', 'latitude']
    if all(di[key] is not None for key in list_keys):
        return di
    else:
        raise KeyError


if __name__ == '__main__':
    a = {
        'category': 'general news',
        'country': 'Canada',
        'city': None,
        'continent': 'North America',
        'country_longitude': -95.7129,
        'country_latitude': 45.4215
    }
    print(validate_keys(a))