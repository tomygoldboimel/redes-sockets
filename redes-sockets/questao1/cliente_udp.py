import socket
PORTA = 10417

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'Ola Servidor UDP!', ('localhost', PORTA))
s.close()