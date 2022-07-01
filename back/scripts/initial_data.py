from datetime import date


def main():
    import sys

    sys.path.insert(0, "")

    from domain.barcode import BarCode, BarCodeRepository

    database_path = "data/database.db"

    barcode_repository = BarCodeRepository(database_path)

    first_palot = BarCode(lote_number="K2100017001", project="L.CALIBRADO", date="")
    barcode_repository.save_palot(first_palot)


if __name__ == "__main__":
    main()
