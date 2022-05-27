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
        good_body = body["lote_number"].replace("'", "-")
        bar_code_unconverted = BarCode(
            project=body["project"],
            lote_number=good_body,
        )
        erp_response =   bar_code_unconverted.send_xml_to_erp()
        if erp_response == "true":
            return erp_response, 200
        else:
            return erp_response, 500
        

    return app
