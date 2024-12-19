from flask import Blueprint

statistic_bluprint = Blueprint('statistic_bluprint', __name__)

@statistic_bluprint.route('/', methods=['GET'])
def get_statistic_bluprint():
    return "hello world"