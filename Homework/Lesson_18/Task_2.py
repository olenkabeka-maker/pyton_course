# Task_2 
"""Реалізуйте 2 класи, перший - Бос, а другий - Працівник. Працівник має властивість 'boss', а її значення має бути екземпляром Boss.
Ви можете перепризначити це значення, але вам слід перевірити, чи нове значення є Boss. Кожен Boss має список своїх власних працівників. 
Вам слід реалізувати метод, який дозволяє додавати працівників до Boss. Вам не дозволено додавати екземпляри класу Boss до списку 
працівників безпосередньо через доступ до атрибута, натомість використовуйте геттери та сеттери!"""

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []                                  # список працівників

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if not isinstance(worker, Worker):                  # Додає робітника тільки через перевірку класу Worker
            raise TypeError("Можна додавати лише об'єкти Worker")
        
        if worker not in self._workers:                     # Перевірка, чи робітник вже не має цього боса
            worker.boss = self                              # використовується сетер в Worker

    def __repr__(self):
        return f"Boss({self.name})"

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss                                    # використання сетера для перевірки

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("boss повинен бути об'єктом класу Boss")
        
        if self._boss and self in self._boss.workers:
            self._boss.workers.remove(self)
        
        self._boss = new_boss
        
        if self not in new_boss.workers:                    # автоматично додаєм робітника до боса, якщо його ще там немає
            new_boss._workers.append(self)

    def __repr__(self):
        return f"Worker({self.name})"


boss1 = Boss(1, "Катя", "Техкорп")
boss2 = Boss(2, "Семен", "Технокарп")

worker1 = Worker(101, "Макс", "Техкорп", boss1)
worker2 = Worker(102, "Альона", "Техкорп", boss1)

print("Працівники Каті:", boss1.workers)
print("Працівники Семена:", boss2.workers) 


worker1.boss = boss2                                        # Зміна боса
print("\nПісля зміни боса для Макса:")
print("Працівники Каті:", boss1.workers)
print("Працівники Семена:", boss2.workers)

worker3 = Worker(103, "Віктор", "Технокарп", boss2)         # Додаєм робітника через метод боса
boss2.add_worker(worker2)                                   # переводжу worker2 до boss2

print("\nПісля переводу Альони:")
print("Працівники Каті:", boss1.workers)
print("Працівники Семена:", boss2.workers)  