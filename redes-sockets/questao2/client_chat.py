import socket

PORTA = 10417

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', PORTA))

while True:
    msg = input('Cliente: ')
    s.send(msg.encode())
    if msg.lower() == 'sair':
        break
    resposta = s.recv(1024).decode()
    if resposta.lower() == 'sair':
        print('Servidor encerrou a conexão.')
        break
    print('Servidor:', resposta)

s.close()