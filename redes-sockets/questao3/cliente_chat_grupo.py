import socket
import threading

PORTA = 10417
HOST = 'localhost'

def receber_mensagens(s):
    while True:
        try:
            msg = s.recv(1024).decode()
            if msg:
                print(msg)
        except:
            print('Conexão encerrada.')
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORTA))

pedido_nome = s.recv(1024).decode()
print(pedido_nome, end='')
nome = input()
s.send(nome.encode())

thread = threading.Thread(target=receber_mensagens, args=(s,))
thread.daemon = True
thread.start()

print('Conectado ao chat! Digite "sair" para sair.')

while True:
    msg = input()
    s.send(msg.encode())
    if msg.lower() == 'sair':
        break

s.close()