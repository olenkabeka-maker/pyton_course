"""Розширити несортований список. Реалізуйте методи append, index, pop, insert для UnsortedList. 
Також реалізуйте метод slice, який прийматиме два параметри 'start' та 'stop' та повертатиме копію списку, 
починаючи з позиції та до позиції stop, але не включаючи її."""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, item):                         # додає елемент у кінець списку
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def index(self, item):                          # повертає позицію елемента у списку (з 0). Якщо немає — викликає помилку
        
        current = self.head
        pos = 0
        while current:
            if current.data == item:
                return pos
            current = current.next
            pos += 1
        raise ValueError(f"{item} не знайдено у списку")

    def pop(self, pos=None):                        # видаляє та повертає елемент за позицією. Якщо позиція не задана — видал. остан.
        if self.head is None:
            raise IndexError("pop з порожнього списку")
        
        if pos == 0:                                # якщо треба видалити перший елемент
            data = self.head.data
            self.head = self.head.next
            return data

        prev = None
        current = self.head
        index = 0
        while current.next and (pos is None or index < pos):
            prev = current
            current = current.next
            index += 1

        
        if pos is not None and index < pos:         # якщо pos не заданий — current уже останній елемент
            raise IndexError("індекс поза межами списку")

        data = current.data
        prev.next = current.next
        return data

    def insert(self, pos, item):                    # вставляє елемент у вказану позицію
        new_node = Node(item)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0
        prev = None
        while current and index < pos:
            prev = current
            current = current.next
            index += 1

        if prev is None:
            raise IndexError("позиція поза межами списку")

        new_node.next = current
        prev.next = new_node

    def slice(self, start, stop):                   # повертає копію списку з позиції start до stop (не включно)        
        new_list = UnsortedList()
        current = self.head
        index = 0

        while current and index < stop:
            if index >= start:
                new_list.append(current.data)
            current = current.next
            index += 1
        return new_list

    def show(self):                                 # друкує елементи списку
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ul = UnsortedList()
ul.append(10)
ul.append(20)
ul.append(30)
ul.append(40)
ul.append(50)

print("Початковий список:")
ul.show()

ul.insert(2, 25)
print("Після вставки 25 у позицію 2:")
ul.show()

print("Індекс елемента 40:", ul.index(40))

print("Видалено елемент:", ul.pop(3))
ul.show()

print("Слайс (з 1 по 3):")
slice_list = ul.slice(1, 3)
slice_list.show()