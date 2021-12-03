from Core.ConfigConnection import ConfigConnection
from Core.MySQLEngine import MySQLEngine
from Core.menu_principal import Welcome_screen_Game

config_file = ConfigConnection()
mysqlEngine = MySQLEngine(config_file)

def start_program():
    app = Welcome_screen_Game()
    app.ShowGame()
    

if __name__ == "__main__":
    start_program()


