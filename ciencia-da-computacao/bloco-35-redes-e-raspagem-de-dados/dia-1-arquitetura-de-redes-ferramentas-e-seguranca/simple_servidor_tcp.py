from socketserver import StreamRequestHandler, TCPServer


class TCPHandler(StreamRequestHandler):
    pass


if __name__ == "__main__":
    server_address = ("localhost", "8080")
    with TCPServer(server_address, TCPHandler) as server:
        server.serve_forever()
