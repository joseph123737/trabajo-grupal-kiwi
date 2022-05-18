from crypt import methods
from flask import Flask, request
from flask_cors import CORS
from src.domain.bar_code import BarCode


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/barcode", methods=["POST"])
    def get_bar_code():
        body = request.json
        print(body)

        bar_code_unconverted = BarCode(
            project=body["project"],
            lote_number=body["lote_number"],
        )
        return "", 200

    return app
