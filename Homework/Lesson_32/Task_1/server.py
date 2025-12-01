import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # створюю UDP-сокет

server.bind((UDP_IP, UDP_PORT))                             # прив’язую сервер до IP і порту

print("UDP server is running...")

while True:
    data, addr = server.recvfrom(BUF_SIZE)
    print("Received:", data.decode(), "from", addr)
    
    server.sendto(data, addr)                               # відправляювідповідь клієнту