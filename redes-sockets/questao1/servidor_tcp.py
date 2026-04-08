import socket
PORTA = 10417
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORTA))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024)
print('Dado Recebido:', data.decode())
conn.close()