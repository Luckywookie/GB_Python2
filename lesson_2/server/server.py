import socketserver
from struct import *


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        print('Клиент {} пишет: {}'.format(self.client_address, self.data))
        p = unpack('2s6s6s4s4sii', self.data)
        _date = int(p[1], 16)
        year = (_date & 0xfe00) >> 9
        month = (_date & 0x1f0) >> 5
        day = _date & 0x1f
        print('Дата: 20{}.{}.{}'.format(year, month, day))
        _time= int(p[2], 16)
        hour = (_time & 0x1f000) >> 12
        mins = (_time & 0xfc0) >> 6
        sec = _time & 0x3f
        print('Время: {}:{}:{}'.format(hour, mins, sec))
        print('Тип транзакции: {}, команда: {}'.format(p[3], p[4]))
        print('Терминал: {}, операция: {}'.format(p[5], p[6]))

    def finish(self):
        pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print('Сервер запущен')
    serv.serve_forever()




