import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 10417))
data, addr = s.recvfrom(1024)
print('Dado Recebido:', data.decode())