from flask import Blueprint, jsonify

from statistics_app.services.routes_services.statistic_route_services.get_deadliest_attack_service import *

statistic_bluprint = Blueprint('statistic_bluprint', __name__)


@statistic_bluprint.route('/deadliest-attack', methods=['GET'])
def get_deadliest_attack_endpoint():
    try:
        return jsonify(get_deadliest_attack_endpoint_service()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_bluprint.route('/deadliest-attack/<int:limit>', methods=['GET'])
def get_limit_deadliest_attack_endpoint(limit):
    try:
        return jsonify(get_deadliest_attack_endpoint_service(limit)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_bluprint.route('/average-casualties-by/<string:target>', methods=['GET'])
def get_average_casualties_by_region_endpoint(target):
    try:
        return jsonify(get_average_fatal_by(target)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_bluprint.route('/top-5-groups-by-attacks', methods=['GET'])
def get_top_5_groups_by_attacks_endpoint():
    try:
        return jsonify(get_top_5_groups_by_attacks()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_bluprint.route('/region/attack-change-percentage', methods=['GET'])
def get_attack_change_percentage_by_region_endpoint():
    try:
        return jsonify(get_attack_change_percentage_by_region()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_bluprint.route('/regions/most-active-groups', methods=['GET'])
def get_most_active_groups_by_region_endpoint():
    try:
        return jsonify(get_most_active_groups_by_region()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500