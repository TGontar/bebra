import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
sock.send(bytes('hello, bebra', encoding='UTF-8'))

data = sock.recv(1024)
sock.close()

print(str(data, encoding='UTF-8'))