from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.info import InfoRepository


def test_should_pick_front_json():
    info_repository = InfoRepository(temp_file())
    app = create_app(repositories={"info": info_repository})
    client = app.test_client()

    body = {
        "lote_number": "123456789",
        "proyect": "L.CALIBRADO",
    }

    response = client.post("/api/barCode", json=body)

    assert response.status_code == 200

    assert response.json == {
        "lote_number": "123456789",
        "proyect": "L.CALIBRADO",
        "user_name": "ik",
    }
