from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.info import InfoRepository


def test_should_send_a_xml_to_erp():
    info_repository = InfoRepository(temp_file())
    app = create_app(repositories={"info": info_repository})
    client = app.test_client()

    body = {
        "lote_number": "123456789",
        "project": "L.CALIBRADO",
    }

    response = client.post("/api/barcode", json=body)

    assert response.status_code == 409
