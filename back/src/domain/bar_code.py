class BarCode:
    def __init__(self, proyect, lote_number):
        self.proyect = proyect
        self.lote_number = lote_number
        self.user_name = "ik"

    def to_dict(self):
        return {
            "proyect": self.proyect,
            "lote_number": self.lote_number,
            "user_name": self.user_name,
        }
