import socketserver
from struct import *


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        print('Клиент {}'.format(self.client_address))
        # Пример строки: zz   0x228b   0xf124  0x00  0x00   \x00\x00@\xe2\x01\x00\x8d\xe3\x01\x00
        p = unpack('2s6s6s4s4s4i', self.data)
        _date = int(p[1], 16)   # дата
        year = (_date & 0xfe00) >> 9
        month = (_date & 0x1f0) >> 5
        day = _date & 0x1f
        _time= int(p[2], 16)   # время
        hour = (_time & 0x1f000) >> 12
        mins = (_time & 0xfc0) >> 6
        sec = _time & 0x3f
        print('Дата: 20{}.{}.{} {}:{}:{}'.format(year, month, day, hour, mins, sec))
        print('Тип транзакции: {}, команда: {}'.format(p[3], p[4]))
        print('Терминал: {}, операция: {}'.format(p[5], p[6]))
        if p[3] == b'0x00':
            print('Сервисная транзакция')
        elif p[3] == b'0x01':
            print('Платёжная транзакция')
            pay = int(p[8])/100
            print('Компания: {}, сумма: {} руб'.format(p[7], pay))
        elif p[3] == b'0x02':
            print('Инкассация')


    def finish(self):
        pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
    # print('Сервер запущен')
    # serv.serve_forever()
    try:
        serv = socketserver.TCPServer((HOST, PORT), TCPHandler)
        print("Server started")
        serv.serve_forever()
    except KeyboardInterrupt:  # control-C
        print("exit")




