import mysql.connector 
from tabulate import tabulate

class MySQLEngine:
    def __init__(self,configConnection):
        #Se genera la conexion con la base de datos
        self.dbConnector = mysql.connector.connect(
            host = configConnection.host,
            port = configConnection.port,
            user = configConnection.user,
            password = configConnection.password,
            database = configConnection.database
        )

        self.link = self.dbConnector.cursor()

    def select(self,query=""):
        self.link.execute(query)
        return self.link.fetchall()


    def printAsTable(self,result,headers=[]):

        if not headers:
            print (tabulate(result))
            else
            print (tabulate(result,headers=headers))