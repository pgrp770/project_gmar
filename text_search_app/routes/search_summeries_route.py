from flask import Blueprint, make_response

from text_search_app.db.elastic_db.repositories.summery_repository import *
from text_search_app.services.map_services.send_html_maps_service import create_map

search_summery_blueprint = Blueprint('search_summery_blueprint', __name__)


@search_summery_blueprint.route('/<string:keywords>', methods=['GET'])
def search_summeries(keywords: str):
    result = search_by_words("summeries", keywords)
    response = make_response(create_map(result))
    return response


@search_summery_blueprint.route('/historic/<string:keywords>', methods=['GET'])
def search_historic_summeries(keywords: str):
    result = search_by_category("summeries", keywords, "historical terror attack")
    response = make_response(create_map(result))
    return response


@search_summery_blueprint.route('/nowadays/<string:keywords>', methods=['GET'])
def search_nowadays_summeries(keywords: str):
    result = search_by_category("summeries", keywords, "nowadays terror attack")
    print(result)
    response = make_response(create_map(result))
    return response


@search_summery_blueprint.route('/dates/<string:start>/<string:finish>/<string:keywords>', methods=['GET'])
def search_summeries_by_dates(start, finish, keywords: str):
    result = search_by_summary_and_date("summeries", keywords, start, finish)
    response = make_response(create_map(result))
    return response
