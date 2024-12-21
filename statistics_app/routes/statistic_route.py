from flask import Blueprint, jsonify, request, Response, make_response
import folium

from statistics_app.services.routes_services.statistic_route_services.statistic_route_service import *
from statistics_app.services.routes_services.folium_map_services.send_html_maps_service import e_2, e_6, e_11, e_14, \
    e_16, e_8

statistic_bluprint = Blueprint('statistic_bluprint', __name__)


# e_1
@statistic_bluprint.route('/deadliest-attack', methods=['GET'])
def get_deadliest_attack_endpoint():
    try:
        return jsonify(get_deadliest_attack_endpoint_service(int(request.args.get('limit', 0)))), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500



# e_2
# @statistic_bluprint.route('/average-casualties-by/<string:target>', methods=['GET'])
# def get_average_casualties_by_region_endpoint(target):
#     try:
#         a = get_average_casualties(target, int(request.args.get('limit', 0)))
#
#         return try_one(a).get_root().render() , 200
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500

@statistic_bluprint.route('/average-casualties-by/<string:target>', methods=['GET'])
def get_average_casualties_by_region_endpoint(target):
    try:
        data = get_average_casualties(target, int(request.args.get('limit', 0)))
        response = make_response(e_2(data))
        return response
    except Exception as e:
        return jsonify({'message': str(e)}), 500




# e_3
@statistic_bluprint.route('/top-5-groups-by-attacks', methods=['GET'])
def get_top_5_groups_by_attacks_endpoint():
    try:
        return jsonify(get_top_5_groups_by_attacks()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_6
@statistic_bluprint.route('/region/attack-change-percentage', methods=['GET'])
def get_attack_change_percentage_by_region_endpoint():
    try:
        data = get_attack_change_percentage_by_region()
        response = make_response(e_6(data))
        return response
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_8
@statistic_bluprint.route('/regions/most-active-groups', methods=['GET'])
def get_most_active_groups_by_region_endpoint():
    try:
        data = get_most_active_groups_by_region()
        response = make_response(e_8(data))
        return response
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_11
@statistic_bluprint.route('/region/region-targets-intersection/<string:target>', methods=['GET'])
def get_region_targets_intersection_endpoint(target: str):
    try:
        data = get_region_targets_intersection(target)
        return make_response(e_11(data))
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_13
@statistic_bluprint.route('/groups/involved-in-same-attacks', methods=['GET'])
def get_groups_involved_in_same_attacks_endpoint():
    try:
        return jsonify(get_groups_involved_in_same_attacks()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_14
@statistic_bluprint.route('/regions/shared-attack-strategies/<string:target>', methods=['GET'])
def get_shared_attack_strategies_by_region_endpoint(target):
    try:
        data = get_shared_attack_strategies_by_region(target)
        return make_response(e_14(data))
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_16
@statistic_bluprint.route('/regions/high-intergroup-activity/<string:target>', methods=['GET'])
def get_high_intergroup_activity_by_region_endpoint(target):
    try:
        data = get_high_intergroup_activity_by_region(target)
        return make_response(e_16(data))
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# e_19
@statistic_bluprint.route('/groups/similar-goals-timeline', methods=['GET'])
def get_similar_goals_timeline_by_group_endpoint():
    try:
        return jsonify(get_similar_goals_timeline_by_group()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
