from flask import Flask

# from statistics_app.routes.addvanced_statistcs_route import advanced_statistic_bluprint
from statistics_app.routes.statistic_route import statistic_bluprint

app = Flask(__name__)
app.register_blueprint(statistic_bluprint, url_prefix='/api/statistics')
# app.register_blueprint(advanced_statistic_bluprint, url_prefix='/api/advanced_statistics')


if __name__ == '__main__':
    app.run(debug=True, port=5000)