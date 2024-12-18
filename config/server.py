from app.utils import read_yaml


server = read_yaml()['server']


class ServerConfig:
    SERVER_HOST = server['host']
    SERVER_PORT = server['port']