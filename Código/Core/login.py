

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
name = config['DEFAULT']['DB_NAME']
print(name)
