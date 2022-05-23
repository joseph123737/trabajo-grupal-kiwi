from crypt import methods
from flask import Flask, request
from flask_cors import CORS
from src.domain.bar_code import BarCode, converted_json_to_xml
from src.lib.utils import object_to_json
import xml.etree.cElementTree as e
import json


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
        barcode_to_xml = converted_json_to_xml(body)
        barcode_unconverted = BarCode(
            project=body["project"],
            lote_number=body["lote_number"],
        )

        return object_to_json(barcode_unconverted), 200

    return app
