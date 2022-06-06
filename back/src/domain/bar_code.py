import io
import xml.etree.cElementTree as ET
import pycurl
import sqlite3
from config import url


class BarCode:
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
        headers = [
            "Method: POST",
            "Connection: Keep-Alive",
            "User-Agent: PHP-SOAP-CURL",
            "Content-Type: text/xml; charset=utf-8",
            'SOAPAction:"CheckConsumption"',
        ]
        body_to_send = f"""<?xml version="1.0" encoding="UTF-8"?>
	              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:app="urn:microsoft-dynamics-schemas/codeunit/APP_MGMT">
	              <soapenv:Header/>
	              <soapenv:Body>
		              <app:CheckConsumption>
			            <app:pJobNo>{self.project}</app:pJobNo>
			            <app:pBarcode>{self.lote_number}</app:pBarcode>
			            <app:pResourceNo >IK</app:pResourceNo >
		              </app:CheckConsumption>
	              </soapenv:Body>
	              </soapenv:Envelope>"""

        curl = pycurl.Curl()
        buffer = io.BytesIO()

        curl.setopt(
            pycurl.URL,
            url,
        )
        curl.setopt(pycurl.HTTPHEADER, headers)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, body_to_send)
        curl.setopt(pycurl.WRITEDATA, buffer)

        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_NTLM)
        curl.setopt(pycurl.USERPWD, "GARAIAKOOP\\navision:Navi@GaraiaKoop")
        curl.perform()
        curl.close()

        response = buffer.getvalue()
        body = response.decode("iso-8859-1")

        root = ET.fromstring(body)
        result = []
        for body in root:
            for fault in body:
                for faultstring in fault:
                    result.append(faultstring.text)

        if len(result) == 1:
            good_result = result[0]
            status_code = 200
        else:
            good_result = result[1]
            status_code = 500
        dict_to_return = {"status_code": status_code, "response": good_result}
        return dict_to_return

    def send_error_to_erp(self, error_mensage):
        headers = [
            "Method: POST",
            "Connection: Keep-Alive",
            "User-Agent: PHP-SOAP-CURL",
            "Content-Type: text/xml; charset=utf-8",
            'SOAPAction:"SendErrorConsume"',
        ]
        body_to_send = f"""<?xml version="1.0" encoding="UTF-8"?>
	              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:app="urn:microsoft-dynamics-schemas/codeunit/APP_MGMT">
	              <soapenv:Header/>
	              <soapenv:Body>
		              <app:SendErrorConsume>
			            <app:pJobNoConsume>{self.project}</app:pJobNoConsume>
			            <app:pBarcodeConsume>{self.lote_number}</app:pBarcodeConsume>
			            <app:pResourceNoConsume>IK</app:pResourceNoConsume>
                        <app:pErrorConsume>{error_mensage}</app:pErrorConsume>
		              </app:SendErrorConsume>
	              </soapenv:Body>
	              </soapenv:Envelope>"""

        curl = pycurl.Curl()
        curl.setopt(
            pycurl.URL,
            url,
        )
        curl.setopt(pycurl.HTTPHEADER, headers)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, body_to_send)

        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_NTLM)
        curl.setopt(pycurl.USERPWD, "GARAIAKOOP\\navision:Navi@GaraiaKoop")

        curl.perform()
        curl.close()


class BarCodeRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists palots (
                lote_number varchar,
                project varchar,
                status_code varchar,
                response varchar,
                date varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def get_palots(self):
        sql = """select * from palots"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            palot = BarCode(**item)
            result.append(palot)

        return result

    def save_palot(self, palot):
        sql = """insert into palots (lote_number, project,status_code,response, date) values (
            :lote_number, :project,:status_code,:response, DATE()
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "lote_number": palot["lote_number"],
                "project": palot["project"],
                "status_code": palot["status_code"],
                "date": palot["date"],
                "response": palot["response"],
            },
        )
        conn.commit()
        conn.close()
