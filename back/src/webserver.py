from flask import Flask, request
from flask_cors import CORS
from src.domain.bar_code import BarCode
import xml.etree.cElementTree as e


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/barcode", methods=["POST"])
    def get_bar_code():
        body = request.json

        bar_code_unconverted = BarCode(
            project=body["project"],
            lote_number=body["lote_number"],
        )
        bar_code_unconverted.send_xml_to_erp()
        return "", 200

    return app
