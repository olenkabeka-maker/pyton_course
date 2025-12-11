import socket
import threading

def handle_client(conn, addr):
    print(f"[+] Нове з'єднання: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # echo
    print(f"[-] З'єднання розірвано: {addr}")

def run_server(host="127.0.0.1", port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Сервер запущено на {host}:{port}")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        print("\nСервер зупинено вручну.")
    finally:
        server.close()

if __name__ == "__main__":
    run_server()