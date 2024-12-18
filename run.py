from app.__init__ import create_server
import os
server = create_server()
print(os.getcwd())

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080, debug=True)
