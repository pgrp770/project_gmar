from flask import Blueprint, jsonify, make_response
import folium

from text_search_app.db.elastic_db.repositories.summery_repository import search_by_words, search_by_type, \
    search_by_summary_and_date

search_summery_blueprint = Blueprint('search_summery_blueprint', __name__)


def create_map(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    for row in data:
        if row.get('latitude') and row.get('longitude'):
            folium.Marker(
                location=(row['latitude'], row['longitude']),
                popup=(
                    f"<b>Content:</b> {row.get('content', 'N/A')}<br>"
                    f"<b>Country:</b> {row.get('country', 'N/A')}<br>"
                    f"<b>Region:</b> {row.get('region', 'N/A')}<br>"
                    f"<b>Date:</b> {row.get('date', 'N/A')}"
                    f"<b>Category:</b> {row.get('category', 'N/A')}<br>"
                )
            ).add_to(m)

    return m._repr_html_()
@search_summery_blueprint.route('/<string:keywords>', methods=['GET'])
def search_summeries(keywords: str):
    result = search_by_words("summeris",keywords)
    response = make_response(create_map(result))
    return response


@search_summery_blueprint.route('/historic/<string:keywords>', methods=['GET'])
def search_historic_summeries(keywords: str):
    result = search_by_type("summeris",keywords, "historical terror attack")
    response = make_response(create_map(result))
    return response


@search_summery_blueprint.route('/nowadays/<string:keywords>', methods=['GET'])
def search_nowadays_summeries(keywords: str):
    result = search_by_type("summeris",keywords, "nowadays terror attack")
    print(result)
    response = make_response(create_map(result))
    return response

@search_summery_blueprint.route('/dates/<string:start>/<string:finish>/<string:keywords>', methods=['GET'])
def search_summeries_by_dates(start, finish, keywords: str):

    result = search_by_summary_and_date("summeris",keywords, start, finish)
    response = make_response(create_map(result))
    return response
