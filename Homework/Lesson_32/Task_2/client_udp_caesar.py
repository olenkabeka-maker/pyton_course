import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Введіть повідомлення: ")
key = int(input("Введіть ключ шифрування (ціле число): "))

send_data = f"{key}|{message}"

sock.sendto(send_data.encode(), (UDP_IP, UDP_PORT))

data, _ = sock.recvfrom(1024)
print("Отримано від сервера (зашифровано):", data.decode())