from Core.ConfigConnection import ConfigConnection
from Core.MySQLEngine import MySQLEngine
from Core.login import Login

config_file = ConfigConnection()
mysqlEngine = MySQLEngine(config_file)

def start_program():
    app = Login()
    app.show_login()
    

if __name__ == "__main__":
    start_program()


