from db import Base, session
from datetime import datetime, date
import socketserver
import threading
from struct import *
from models.payments import PaymentModel
from models.partners import PartnerModel
from models.terminals import TerminalModel


class TCPHandlerThread(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, self.data), 'utf-8')
        self.request.sendall(response)
        print('Клиент {}'.format(self.client_address))
        # Пример строки: zz   0x228b   0xf124  0x00  0x00   \x00\x00@\xe2\x01\x00\x8d\xe3\x01\x00
        p = unpack('!2s6s6s4s4s4i', self.data)
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
            transaction = PaymentModel(datetm=date(year, month, day),
                                       terminal_id=int(p[5]),
                                       transaction_id=int(p[6]),
                                       partner_id=int(p[7]),
                                       summ=int(p[8]))
            transaction.save_to_db()
            print('Saved to BD')
        elif p[3] == b'0x02':
            print('Инкассация')

    def finish(self):
        pass


# Обратите внимание на использование класса-примеси ThreadingMixIn
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
        Потоковый сервер. Достаточно создать класс без "внутренностей"
    """
    pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = ThreadedTCPServer((HOST, PORT), TCPHandlerThread)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever,
                                     name='thread.server')
    # server_thread.daemon = True
    try:
        server_thread.start()
        print("Сервер запущен в потоке: {} по адресу {}:{}".format(server_thread.name, ip, port))
    except KeyboardInterrupt:  # control-C
        server.shutdown()
        print("exit")




