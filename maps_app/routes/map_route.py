from flask import Blueprint, render_template

maps_blueprint = Blueprint('map', __name__, url_prefix='/api/maps')


@maps_blueprint.route('/statistics', methods=['GET'])
def render_statistics_maps():
    return render_template('statistics_maps.html')


@maps_blueprint.route('/text_search', methods=['GET'])
def render_text_search_maps():
    return render_template('text_search_map.html')
