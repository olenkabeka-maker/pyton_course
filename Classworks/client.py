import socket

T_PORT = 1060
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024

MSG = "Hello karl"

k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # створюємо сокет об_єкт 'k'

k.connect((TCP_IP, T_PORT))

k.send(MSG.encode())     # відправити повідомлення as bytes

data = k.recv(BUF_SIZE)  # отримати відповіді

print("Received:", data.decode())

k.close()