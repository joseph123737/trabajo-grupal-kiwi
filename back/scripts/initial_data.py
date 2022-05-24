from datetime import date


def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.bar_code import BarCode, BarCodeRepository


    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    barcode_repository = BarCodeRepository(database_path)

    info_repository.save(Info(app_name="f5-seed-app"))

    first_palot = BarCode(
        lote_number= "K2100017001",
        project= "L.CALIBRADO",
        date = ""
    )
    barcode_repository.save_palot(first_palot)


if __name__ == '__main__':
    main()
