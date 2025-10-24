# Task_4    Custom exception

class CustomException(Exception):
    
    def __init__(self, msg):
        
        super().__init__(msg)                               # Викликаємо __init__ для класу Exception
        with open("logs.txt", "a", encoding="utf-8") as f:  # Записуємо повідомлення у файл
            f.write(msg + "\n")

try:
    raise CustomException("Помилка: неможливо додати товар з від’ємною ціною.")
except CustomException as e:
    print(f"Піймала виняток: {e}")