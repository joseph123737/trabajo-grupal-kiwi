from crypt import methods
from flask import Flask, request
from flask_cors import CORS
from src.domain.bar_code import BarCode
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/barcode", methods=["POST"])
    def get_bar_code():
        body = request.json
        print(body)

        bar_code_unconverted = Barcode(
            proyect=body["proyect"],
            lote_number=body["lote_number"],
        )
        return object_to_json(bar_code_unconverted), 200

    return app
