class BarCode:
    def __init__(self, project, lote_number):
        self.project = project
        self.lote_number = lote_number
        self.user_name = "ik"

    def to_dict(self):
        return {
            "project": self.project,
            "lote_number": self.lote_number,
            "user_name": self.user_name,
        }
