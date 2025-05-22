import configparser
config = configparser.ConfigParser()
config['Settings'] = {'working_directory': "D:\dzhie\Documents\криптография"}
with open('config.ini', 'w') as configfile:
  config.write(configfile)