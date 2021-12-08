#Conexion SQL
from math import e
import pyodbc

class clsSQL(object):
 
    def __init__(self):
        self.conexion = None
        self.server = 'localhost'
        self.bd = 'db-IGP'
        self.usuario = 'user_BI'
        self.password = 'UPT-bi-2021'
        self.estado = self.sqlConnect()
        
    def sqlConnect(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};'
                            + 'SERVER='+ self.server + ';'  
                            + 'DATABASE='+ self.bd + ';' 
                            + 'UID='+ self.usuario + ';' 
                            + 'PWD='+ self.password )
            return True
        except:
            return False
        
    def sqlQuery(self, query):
        datos = []
        if self.estado == True:
            cursor = self.conexion.cursor()
            try:
                cursor.execute(query)
                datos = cursor.fetchall()
                cursor.close()
                return datos
            except:
                cursor.close()
                return datos.append('No se encontraron datos')

    def sqlInsert(self, query):
        if self.estado == True:
            cursor = self.conexion.cursor()
            try:
                cursor.execute(query)
                print("Registro exitoso")
            except:
                print("Error al registrar ")
            cursor.commit()
            cursor.close()

#sql = clsSQL()
#print(sql.estado)
#sql.sqlInsert("INSERT INTO Test (ID, Text, Url) VALUES ( 122, 'test\n holi', 'url.test.com');")

#print(len("102 km al O de Pastaza, Alto Amazonas - Loreto"))