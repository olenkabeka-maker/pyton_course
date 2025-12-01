import socket

def caesar_cipher(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP Caesar server is running...")

while True:
    data, addr = sock.recvfrom(1024)
    decoded = data.decode()

    # треба формат: "KEY|MESSAGE"
    try:
        key_str, message = decoded.split("|", 1)
        key = int(key_str)
    except:
        sock.sendto("ERROR: Format KEY|MESSAGE".encode(), addr)
        continue

    encrypted = caesar_cipher(message, key)
    sock.sendto(encrypted.encode(), addr)