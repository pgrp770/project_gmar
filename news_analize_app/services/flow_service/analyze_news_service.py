from news_analize_app.api.groq_api import post_groq_api

import toolz as tz

from news_analize_app.api.news_api import main
from news_analize_app.services.coordinates_services import get_lat_lon_from_address
from news_analize_app.utils.validation_utils import validate_groq_json, validate_keys


def analyze_one_article(article: dict):
    try:
        try_a = post_groq_api(article)
        location_dict = tz.pipe(
            try_a,
            validate_groq_json,
            validate_keys
        )
        return {
            "content": article["title"] + article["body"],
            "date": article["date"],
            "category": location_dict["category"],
            "country": location_dict["country"],
            "region": location_dict["region"],
            "latitude": location_dict["latitude"],
            "longitude": location_dict["longitude"],
        }
    except Exception as e:
        print(e)
        return None


def analyze_all_articles():
    return tz.pipe(
        main()['articles']['results'],
        tz.partial(map, analyze_one_article),
        tz.partial(filter, lambda x: bool(x)),
        list
    )


if __name__ == '__main__':
    result = analyze_all_articles()
    print(result)
