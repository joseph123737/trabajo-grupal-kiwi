from src.lib.utils import temp_file
from src.webserver import create_app
from fake_barcodes import BarCodeDuplicated, BarCodeMissing
from src.domain.barcode import BarCodeRepository


def test_should_send_a_xml_to_erp():
    bar_code_repository = BarCodeRepository(temp_file())
    app = create_app(repositories={"erp": bar_code_repository})
    client = app.test_client()

    body = {
        "lote_number": "123456789",
        "project": "L.CALIBRADO",
    }

    response = client.post("/api/barcode", json=body)

    assert response.status_code == 500
