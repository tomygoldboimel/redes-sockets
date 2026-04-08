import socket

PORTA = 10417

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORTA))
s.listen(1)
conn, addr = s.accept()
print('Conexão estabelecida com:', addr)

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'sair':
        print('Encerrando conexão com:', addr)
        break
    print('Cliente:', msg)
    resposta = input('Servidor: ')
    conn.send(resposta.encode())
    if resposta.lower() == 'sair':
        break

conn.close()
s.close()