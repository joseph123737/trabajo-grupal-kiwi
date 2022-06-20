from datetime import date
from flask import Flask, request
from flask_cors import CORS
from src.domain.barcode import BarCode, BarCodeRepository


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/barcode", methods=["POST"])
    def get_barcode():
        body = request.json
        good_body = body["lote_number"].replace("'", "-")
        barcode_unconverted = repositories["erp"](
            project=body["project"],
            lote_number=good_body,
        )
        erp_response = barcode_unconverted.send_xml_to_erp()
        dict_to_save = {
            "status_code": erp_response["status_code"],
            "project": barcode_unconverted.project,
            "lote_number": barcode_unconverted.lote_number,
            "response": erp_response["response"],
            "date": barcode_unconverted.date,
        }
        repositories["barcode"].save_palot(dict_to_save)
        if erp_response["status_code"] == 200:
            return erp_response, 200
        if erp_response["status_code"] == 500:
            barcode_unconverted.send_error_to_erp(erp_response["response"])
            if erp_response["response"].startswith("Bin"):
                return erp_response, 409
            else:
                return erp_response, 404

    return app
