class BarCodeOk:
    def __init__(self, project, lote_number, date=None):
        self.project = project
        self.lote_number = lote_number
        self.date = date
        self.user_name = "IK"

    def to_dict(self):
        return {
            "project": self.project,
            "lote_number": self.lote_number,
            "date": self.date,
            "user_name": self.user_name,
        }

    def send_xml_to_erp(self):
        dict_to_return = {"status_code": 200, "response": "good_result"}
        return dict_to_return

    def send_error_to_erp(self, error_mensage):
        pass


class BarCodeMissing:
    def __init__(self, project, lote_number, date=None):
        self.project = project
        self.lote_number = lote_number
        self.date = date
        self.user_name = "IK"

    def send_xml_to_erp(self):
        dict_to_return = {"status_code": 500, "response": ""}
        return dict_to_return

    def send_error_to_erp(self, error_mensage):
        pass


class BarCodeDuplicated:
    def __init__(self, project, lote_number, date=None):
        self.project = project
        self.lote_number = lote_number
        self.date = date
        self.user_name = "IK"

    def to_dict(self):
        return {
            "project": self.project,
            "lote_number": self.lote_number,
            "date": self.date,
            "user_name": self.user_name,
        }

    def send_xml_to_erp(self):
        dict_to_return = {"status_code": 500, "response": "Bin duplicado"}
        return dict_to_return

    def send_error_to_erp(self, error_mensage):
        pass
