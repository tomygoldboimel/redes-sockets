import socket
PORTA = 10417

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', PORTA))
s.send(b'Ola Servidor TCP!')
s.close()