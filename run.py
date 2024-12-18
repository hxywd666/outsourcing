from app.__init__ import create_server
from config import ServerConfig
import os


server = create_server()
server_config = ServerConfig()
print(os.getcwd())


if __name__ == "__main__":
    server.run(host=server_config.SERVER_HOST, port=server_config.SERVER_PORT, debug=True)