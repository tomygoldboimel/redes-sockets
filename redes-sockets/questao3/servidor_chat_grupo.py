import socket
import threading

PORTA = 10417
HOST = 'localhost'

clientes = []
nomes = []

def broadcast(mensagem, remetente=None):
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.send(mensagem)
            except:
                index = clientes.index(cliente)
                clientes.remove(cliente)
                nomes.pop(index)

def handle_cliente(cliente, endereco):
    print(f'Nova conexão: {endereco}')

    cliente.send('Digite seu nome: '.encode())
    nome = cliente.recv(1024).decode().strip()
    nomes.append(nome)
    clientes.append(cliente)

    print(f'{nome} entrou no chat.')
    broadcast(f'{nome} entrou no chat!'.encode(), cliente)

    while True:
        try:
            msg = cliente.recv(1024).decode()
            if msg.lower() == 'sair':
                index = clientes.index(cliente)
                clientes.remove(cliente)
                nomes.pop(index)
                broadcast(f'{nome} saiu do chat.'.encode())
                print(f'{nome} saiu do chat.')
                cliente.close()
                break
            else:
                broadcast(f'{nome}: {msg}'.encode(), cliente)
                print(f'{nome}: {msg}')
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            nomes.pop(index)
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()
print(f'Servidor rodando na porta {PORTA}...')

while True:
    cliente, endereco = s.accept()
    thread = threading.Thread(target=handle_cliente, args=(cliente, endereco))
    thread.start()
    print(f'Conexões ativas: {threading.active_count() - 1}')