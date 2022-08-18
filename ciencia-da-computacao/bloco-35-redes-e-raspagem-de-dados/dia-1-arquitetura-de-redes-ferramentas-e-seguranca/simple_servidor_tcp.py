from socketserver import StreamRequestHandler, TCPServer


class TCPHandler(StreamRequestHandler):
    def handle(self):  # Método abstrato de StreamRequestHandler
        self.wfile.write(b'Ola, Cliente!\n')


if __name__ == "__main__":
    server_address = ("localhost", "8080")
    with TCPServer(server_address, TCPHandler) as server:
        server.serve_forever()
