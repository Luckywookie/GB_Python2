import socket
from datetime import datetime, time
from struct import pack


# timestamp = datetime.today().timestamp()
# day = datetime.datetime.fromtimestamp(float(p[0]))

HOST, PORT = 'localhost', 9999

print('Клиент запущен')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

now = datetime.now()

_date = hex(((now.year - 2000 << 9) | (now.month << 5) | (now.day & 31)) & 0xFFFFF).encode('utf-8')
_time = hex((now.hour << 12) | (now.minute << 6) | (now.second & 60)).encode('utf-8')
_type = '0x01'.encode()
_command = '0x00'.encode()
_id_terminal = 5
_id_tranz = 123789
_id_company = 1        # id организации
_payment = 1500        # сумма в копейках
_id_inkass = 253          # id сотрудника-инкассатора
_cash = 285332200         # сумма инкассации в копейках


p = pack('!2s6s6s4s4s4i', b'zz', _date, _time, _type, _command, _id_terminal, _id_tranz, _id_company, _payment)
print(p)
sock.sendall(p)
recvd = str(sock.recv(1024), 'utf-8')

print(recvd)
sock.close()

