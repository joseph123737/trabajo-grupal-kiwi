import io
import xml.etree.cElementTree as e
import pycurl
from urllib3 import HTTPResponse


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

    def converted_json_to_xml(self):
        root = e.Element("CheckConsumption")
        e.SubElement(root, "pJobNo").text = self.project
        e.SubElement(root, "pBarcode").text = self.lote_number
        e.SubElement(root, "pResourceNo").text = self.user_name
        xml_string = e.tostring(root)
        xml_bytes = io.BytesIO(xml_string)
        return xml_bytes

    def send_xml_to_erp(self):
        headers = [
            "Method: POST",
            "Connection: Keep-Alive",
            "User-Agent: PHP-SOAP-CURL",
            "Content-Type: text/xml; charset=utf-8",
            'SOAPAction:"CheckConsumption"',
        ]
        curl = pycurl.Curl()
        buffer = io.BytesIO()

        curl.setopt(
            pycurl.URL,
            "http://80.24.99.155:9074/response",
        )
        curl.setopt(pycurl.HTTPHEADER, headers)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.READDATA, self.converted_json_to_xml())
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.perform()
        body = buffer.getvalue()

        print(".----------", body.decode("iso-8859-1"))
        print(curl.getinfo(pycurl.HTTP_CODE))
        curl.close()


prueba = BarCode(project="l", lote_number="12")
prueba.send_xml_to_erp()
