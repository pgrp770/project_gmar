from news_analize_app.api.groq_api import post_groq_api

import toolz as tz

from news_analize_app.db.elastic_db.repositories.generic_functions import create_butch
from news_analize_app.services.elastic_service.butch_service import from_list_to_actions
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
        print(str(e))


def analyze_all_articles(articles):
    return tz.pipe(
        articles,
        tz.partial(map, analyze_one_article),
        tz.partial(filter, lambda x: bool(x)),
        list
    )


def insert_articles_to_elastic(articles):
    tz.pipe(
        analyze_all_articles(articles),
        from_list_to_actions,
        create_butch
    )
