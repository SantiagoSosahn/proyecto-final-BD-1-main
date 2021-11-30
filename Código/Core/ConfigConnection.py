from configparser import ConfigParser
import os
config = ConfigParser()
#Se obtiene la ruta del archivo actual
path = os.path.dirname(__file__)
config.read(path + '\config.ini')

class ConfigConnection:
    def __init__(self):
        self.host = config['DEFAULT']['DB_HOST']
        self.port = config['DEFAULT']['DB_PORT']
        self.user = config['DEFAULT']['DB_USER']
        self.password = config['DEFAULT']['DB_PASSWORD']
        self.database = config['DEFAULT']['DB_NAME']
        

