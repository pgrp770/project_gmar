from flask import Flask

from statistics_app.routes.statistic_route import statistic_bluprint

app = Flask(__name__)
app.register_blueprint(statistic_bluprint, url_prefix='/api/statistics')
if __name__ == '__main__':
    app.run(debug=True)