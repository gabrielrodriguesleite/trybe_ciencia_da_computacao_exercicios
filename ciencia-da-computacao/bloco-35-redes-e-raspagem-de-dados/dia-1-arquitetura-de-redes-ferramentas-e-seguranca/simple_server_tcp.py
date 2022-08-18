from socketserver import StreamRequestHandler, TCPServer


class TCPHandler(StreamRequestHandler):
    def handle(self):  # Método abstrato de StreamRequestHandler
        self.wfile.write(b"Ola, Cliente!\n")
        while True:
            data = self.rfile.readline().strip().decode("UTF-8")
            if not data:
                self.wfile.write(b"Cliente desconectado")
                print("Cliente foi desconectado")
                break
            print(data)


if __name__ == "__main__":
    server_address = ("localhost", 8080)
    with TCPServer(server_address, TCPHandler) as server:
        print("O server está ON")
        server.serve_forever()


# Acessar pelo navegador localhost:8080
# ou pelo terminal com telnet localhost 8080
