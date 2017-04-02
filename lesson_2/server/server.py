import socketserver


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode()
        print('Клиент {} пишет: {}'.format(self.client_address, self.data))

    def finish(self):
        pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print('Сервер запущен')
    serv.serve_forever()




