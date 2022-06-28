from src.webserver import create_app

from src.domain.barcode import BarCode, BarCodeRepository

database_path = "data/database.db"

repositories = {
    "barcode": BarCodeRepository(database_path),
    "erp": BarCode,
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
