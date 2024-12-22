from flask import Flask

from statistics_app.routes.stats_route import statistic_bluprint

app = Flask(__name__)
app.register_blueprint(statistic_bluprint, url_prefix='/api/advanced_statistics')
if __name__ == '__main__':
    app.run(debug=True)