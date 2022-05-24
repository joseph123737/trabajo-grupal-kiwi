import xml.etree.cElementTree as e
import pycurl
import sqlite3


class BarCode:
    def __init__(self, project, lote_number):
        self.project = project
        self.lote_number = lote_number
        self.date = date
        self.user_name = "ik"

    def to_dict(self):
        return {
            "project": self.project,
            "lote_number": self.lote_number,
            "date": self.date,
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
