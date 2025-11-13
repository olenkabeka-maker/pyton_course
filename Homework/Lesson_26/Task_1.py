"""Реалізувати алгоритм бінарного пошуку за допомогою рекурсії"""

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1                                                   # елемент не знайдено
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)     # Часова складність: O(log n)
print("Індекс елемента:", result)                                  # Просторова складність: O(log n) (через рекурсивні виклики стека)

"""Прочитайте про пошук Фібоначчі та імплементуйте його за допомогою Python. 
Визначте складність алгоритму та порівняйте його з бінарним пошуком"""

def fibonacci_search(arr, target):
    n = len(arr)
                                            
    fibMMm2 = 0                         # iніціалізація чисел Фібоначчі
    fibMMm1 = 1                         
    fibM = fibMMm2 + fibMMm1            

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = fibonacci_search(arr, target)                          # Часова складність: O(log n)
print("Індекс елемента:", result)                               # Просторова складність: O(1) — немає рекурсії



"""Реалізувати in (__contains__)та len (__len__)методиHashTable"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0                                          # кількість збережених елементів

    def _hash(self, key):                                       # проста хеш-функція
        return hash(key) % self.size

    def __setitem__(self, key, value):                          # додавання або оновлення елемента
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
                                                    
        for pair in self.table[index]:                          # оновлюємо, якщо ключ уже є
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[index].append([key, value])                  # додаємо нову пару
        self.count += 1

    def __getitem__(self, key):                                 # отримання значення за ключем
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f"Ключ '{key}' не знайдено")

    def __contains__(self, key):                                # перевірка наявності ключа (оператор 'in')
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return True
        return False

    def __len__(self):                                          # повертає кількість елементів у таблиці
        return self.count

    def __repr__(self):                                         # для зручного виведення
        items = []
        for bucket in self.table:
            if bucket:
                items.extend(f"{k}: {v}" for k, v in bucket)
        return "{" + ", ".join(items) + "}"


ht = HashTable()                                                # таблиця

ht["ім'я"] = "Вікторія"
ht["вік"] = 18
ht["місто"] = "Київ"

print(ht) 
print("вік" in ht)        
print("школа" in ht)
print(len(ht))          
print(ht["місто"])                                              # доступ за ключем   