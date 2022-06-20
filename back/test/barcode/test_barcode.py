from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.barcode import BarCodeRepository
from fake_barcodes import BarCodeDuplicated, BarCodeMissing


def test_should_check_that_lotenumber_doesnt_exist():

    barcode_repository = BarCodeRepository(temp_file())
    app = create_app(
        repositories={"barcode": barcode_repository, "erp": BarCodeMissing}
    )
    client = app.test_client()
    body = {
        "lote_number": "42536u7i48o9",
        "project": "L.CALIBRADO",
    }

    response = client.post("/api/barcode", json=body)

    assert response.status_code == 404


def test_should_check_that_lotenumber_exist():

    barcode_repository = BarCodeRepository(temp_file())
    app = create_app(
        repositories={"barcode": barcode_repository, "erp": BarCodeDuplicated}
    )
    client = app.test_client()
    body = {
        "lote_number": "211109-22",
        "project": "L.CALIBRADO",
    }

    response = client.post("/api/barcode", json=body)

    assert response.status_code == 409
