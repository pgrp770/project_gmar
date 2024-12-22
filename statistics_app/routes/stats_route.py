from flask import Blueprint, jsonify, request, make_response

from statistics_app.services.routes_services.folium_map_services.send_html_maps_service import e_2
from statistics_app.services.routes_services.statistic_route_services.statistic_route_service import \
    get_deadliest_attack_endpoint_service, get_average_casualties

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
#         data = get_average_casualties(target, int(request.args.get('limit', 0)))
#         response = make_response(e_2(data))
#         return response
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
