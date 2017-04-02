import socket

HOST, PORT = 'localhost', 9999

print('Клиент запущен')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('Ho-ho-ho!', 'utf-8'))
recvd = str(sock.recv(1024), 'utf-8')

print(recvd)
sock.close()

