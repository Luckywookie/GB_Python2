import socketserver
import datetime
from struct import *


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        print('Клиент {} пишет: {}'.format(self.client_address, self.data))
        p = unpack('2i', self.data)
        # d = self.data.split()[2]
        day = datetime.datetime.fromtimestamp(float(p[0]))
        print(day)

    def finish(self):
        pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print('Сервер запущен')
    serv.serve_forever()




