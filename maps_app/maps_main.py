from flask import Flask

from maps_app.routes.map_route import maps_blueprint

app = Flask(__name__)

app.register_blueprint(maps_blueprint)
if __name__ == '__main__':
    app.run(debug=True, port=5001)
