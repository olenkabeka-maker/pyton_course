class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

hash_table = HashTable()
hash_table.add("name", "Альона")
print(hash_table.get("name"))

print(hash("Альона"))

"""Обробка колізій"""
"""Коли два ключі мають однаковий хеш — замість того, щоб перезаписувати комірку, ми створюємо ланцюжок значень у цій комірці."""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Кожна комірка містить список пар (key, value)
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Простий хеш: залишок від ділення."""
        return hash(key) % self.size

    def add(self, key, value):
        """Додає або оновлює елемент."""
        index = self._hash(key)
        # Перевіримо, чи ключ уже існує — тоді оновлюємо
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Якщо ключа нема — додаємо нову пару
        self.table[index].append((key, value))

    def get(self, key):
        """Повертає значення за ключем або None."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Видаляє елемент за ключем."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False


ht = HashTable()

ht.add("name", "Альона")
ht.add("age", 39)
ht.add("city", "Бердянськ")

# Імітуємо колізію — різні ключі можуть мати однаковий хеш
ht.add("eman", "Настя")  # 'eman' може потрапити в ту саму комірку, що й 'name'

print(ht.get("name"))   
print(ht.get("eman"))   

# Видалення
ht.remove("age")
print(ht.get("age")) 