import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
BUF_SIZE = 1024

message = "Hello from UDP client!"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(message.encode(), (UDP_IP, UDP_PORT)) # надсилаю повідомлення

data, addr = client.recvfrom(BUF_SIZE)              # отримую відповідь
print("Received from server:", data.decode())