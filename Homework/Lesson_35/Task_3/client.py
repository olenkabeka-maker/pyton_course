import socket

def run_client(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Підключено до сервера {host}:{port}")

            
            message = "Привіт, сервер!"         # Відправка повідомлення серверу
            s.sendall(message.encode("utf-8"))

            
            data = s.recv(1024)                 # Отримання відповіді від сервера
            print("Отримано від сервера:", data.decode("utf-8"))

        except ConnectionRefusedError:
            print("Не вдалося підключитися до сервера. Перевірте, чи він запущений.")
        except Exception as e:
            print("Помилка:", e)

if __name__ == "__main__":
    run_client()