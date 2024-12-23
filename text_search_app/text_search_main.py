from flask import Flask

from text_search_app.routes.search_summeries_route import search_summery_blueprint

app = Flask(__name__)

app.register_blueprint(search_summery_blueprint, url_prefix='/api/summery_search')
if __name__ == '__main__':
    app.run(debug=True, port=5002)
