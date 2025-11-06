# Task_1

"""File Context Manager class"""

import datetime

class LoggedOpen:                                                   # клас, який імітує open() та додає логування і лічильник
       
    open_count = 0                                                  # підраховує кількість відкритих файлів

    def __init__(self, filename, mode="r", **kwargs):
        self.filename = filename
        self.mode = mode
        self.kwargs = kwargs
        self.file = None

    def __enter__(self):
        try:                                                        # відкриваю файл
                                                                    
            self.file = open(self.filename, self.mode, encoding="utf-8", **self.kwargs)
            LoggedOpen.open_count += 1
            print(f"Файл '{self.filename}' відкрито у режимі '{self.mode}'. "
                  f"Всього відкриттів: {LoggedOpen.open_count}")
            return self.file
        except Exception as e:                                      # логую помилку, якщо файл не вдалося відкрити
           
            print(f"Помилка під час відкриття файлу '{self.filename}': "
                  f"{e.__class__.__name__} — {e}")
            raise                                                   # щоб тест зловив FileNotFoundError чи іншу помилку

    def __exit__(self, exc_type, exc_val, exc_tb):                  # якщо файл відкритий — закриває його
            
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Файл '{self.filename}' закрито.")
       
        if exc_type:                                                # якщо була помилка у блоці with — також логує її
            print(f"Виникла помилка: {exc_type.__name__}: {exc_val}")
            return False  # не приглушуємо виняток

        return True