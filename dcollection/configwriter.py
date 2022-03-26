from configparser import ConfigParser

config = ConfigParser()

config['mysqllocal'] = {
    'host' : '127.0.0.1',
    'database' : 'dcollectiondb',
    'user' : 'PyLocalAdmin',
    'password' : 'armaarge'
}

config['mysqlremote'] = {
    'host' : '192.168.220.253',
    'database' : 'dcollectiondb',
    'user' : 'RemoteAdmin',
    'password' : 'armaarge'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)