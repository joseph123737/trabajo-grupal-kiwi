import xml.etree.cElementTree as e
import pycurl

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO


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


def converted_json_to_xml(body):
    root = e.Element("CheckConsumption")
    e.SubElement(root, "pJobNo").text = body["project"]
    e.SubElement(root, "plote_numbers").text = body["lote_number"]
    e.SubElement(root, "pResourceNo").text = "ik"
    a = e.ElementTree(root)
    a.write("prueba.xml")


body = {"project": "project", "lote_number": "lote_number"}

converted_json_to_xml(body)


def prueba_ntlm():

    name = "navision"
    pwd = "Navi@GaraiaKoop"
    url = "https://28dbc435-b17e-4503-940f-03a40b4d50a4.mock.pstmn.io/NutriNav2016GaraiaReal/WS/2002%2004%2010%20COPIA%20IK/Codeunit/APP_MGMT"
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)

    curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_NTLM)
    curl.setopt(pycurl.USERPWD, "{}:{}".format(name, pwd))

    curl.perform()
    curl.close()


prueba_ntlm()
