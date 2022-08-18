
from socketserver import DatagramRequestHandler, UDPServer


class UDPHandler(DatagramRequestHandler):
    def handle(self):  # Método abstrato de DatagramRequestHandler
        self.wfile.write(b'Ola, Cliente!\n')
        data = self.rfile.readline().strip().decode('UTF-8')
        print(data)


if __name__ == "__main__":
    server_address = ("localhost", 9093)
    with UDPServer(server_address, UDPHandler) as server:
        server.serve_forever()
