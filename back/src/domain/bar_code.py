import sqlite3

class BarCode:
    def __init__(self, project, lote_number, date):
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
        cursor.execute(sql,{"lote_number":palots.lote_number,"project":palots.project, "date": palots.date} )
        conn.commit()

  