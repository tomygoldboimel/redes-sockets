# Redes de Computadores - Sockets UDP e TCP

Integrantes:
- Tomy Goldberg Boimel - 10417109
- Fernando Cavaleiro Paiva - 10416680

## Como executar o projeto

### Pré-requisitos
- Python 3.x instalado
- Nenhuma biblioteca externa necessária

Para cada questão execute:
```bash
# Para a questão 1, por exemplo
cd questao1
```

### Questão 1 — Análise TCP e UDP
Abra dois terminais e execute na seguinte ordem:

**TCP:**
```bash
# Terminal 1
python questao1/servidor_tcp.py

# Terminal 2
python questao1/cliente_tcp.py
```

**UDP:**
```bash
# Terminal 1
python questao1/servidor_udp.py

# Terminal 2
python questao1/cliente_udp.py
```
Resultado esperado: Mensagem do cliente escrita no terminal do servidor

---

### Questão 2 — Chat simples com encerramento por "sair"
Abra dois terminais e execute:
```bash
# Terminal 1
python questao2/servidor_chat.py

# Terminal 2
python questao2/cliente_chat.py
```
Digite `sair` em qualquer um dos lados para encerrar a conexão.

Resultado esperado: Cliente e servidor permitidos a trocarem mensagens

---

### Questão 3 — Chat em grupo com múltiplos clientes (Threads)
Abra pelo menos três terminais e execute:
```bash
# Terminal 1
python questao3/servidor_chat_grupo.py

# Terminal 2
python questao3/cliente_chat_grupo.py

# Terminal 3
python questao3/cliente_chat_grupo.py
```
Você pode abrir quantos terminais de cliente quiser. Digite `sair` para sair do chat.

Resultado esperado: Chat aberto para mais de um cliente. Mensagens podem ser visualizadas por todos conectados ao servidor.

---

## Vídeos de Demonstração

- **Vídeo 1 (Questões 1 e 2):** [https://youtu.be/VPiEK0yvsfc]
- **Vídeo 2 (Questão 3):** [https://youtu.be/-7kj_s6TOYk]

---

## Observações
- A porta utilizada é `10417` (primeiros 5 dígitos do TIA)
- Todos os testes foram realizados em `localhost`
- Para testar em máquinas diferentes, substitua `localhost` pelo IP da máquina servidora
