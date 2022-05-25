import io
import xml.etree.cElementTree as e
import pycurl
import sqlite3


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
            "http://80.24.99.155:9074/NutriNav2016GaraiaReal/WS/2002%2004%2010%20COPIA%20IK/Codeunit/APP_MGMT",
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

        body = body.replace('<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">', '')
        body = body.replace('<s:Body>', '')
        body = body.replace('</s:Body>', '')
        body = body.replace('<ExportOrderLines_Result xmlns="urn:microsoft-dynamics-schemas/codeunit/eShopExportImport">', '')
        body = body.replace('</ExportOrderLines_Result>', '')
        body = body.replace('</s:Envelope>', '')
        body = body.replace(' xmlns="&lt;urn:microsoft-dynamics-nav/xmlports/eShopOrderLines&gt;"', '')
        body = body.replace('</faultstring>', '')
        body = body.replace('<faultstring>', '')
        body = body.replace('<faultcode ', '')
        body = body.replace('<s:Fault>xmlns:a="urn:microsoft-dynamics-schemas/error">a:Microsoft.Dynamics.Nav.Types.Exceptions.NavNCLDialogException</faultcode>', '')
        

        return {"body":body,"status_code":curl.getinfo(pycurl.HTTP_CODE)}



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
                lote_number varchar primary key,
                project varchar,
                date varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

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

    def save_palot(self, palots):
        sql = """insert into palots (lote_number, project, date) values (
            :lote_number, :project, DATE()
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "lote_number": palots.lote_number,
                "project": palots.project,
                "date": palots.date,
            },
        )
        conn.commit()
