"""Створіть сервер socket echo, який обробляє кожне з'єднання в окремому потоку."""

import socket
import threading


HOST = '127.0.0.1'              
PORT = 5000                                 # порт для прослуховування


def handle_client(conn, addr):
    print(f"[+] Нове підключення від {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)              # echo


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Echo-сервер запущено на {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[Потоків зараз активні]: {threading.active_count() - 1}")       # інформація для відлагодження


if __name__ == "__main__":
    main()