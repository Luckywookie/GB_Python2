import socket
from datetime import datetime
from struct import *


timestamp = datetime.today().timestamp()

HOST, PORT = 'localhost', 9999

print('Клиент запущен')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

p = pack('2i', 0x7A7A, int(timestamp))
sock.sendall(p)
recvd = str(sock.recv(1024), 'utf-8')

print(recvd)
sock.close()

