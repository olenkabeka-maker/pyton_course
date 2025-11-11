"""Реалізуйте чергу, використовуючи однозв'язний список"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None                           # початок черги (де елементи видаляються)
        self.rear = None                            # кінець черги (де додаються)
        self.count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):                        # додає елемент у кінець черги
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node       # якщо черга порожня, новий елемент — і front, і rear
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self):                              # видаляє елемент з початку черги
        if self.is_empty():
            raise IndexError("dequeue з порожньої черги")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:                     
            self.rear = None
        self.count -= 1
        return data

    def peek(self):                                 # повертає перший елемент без видалення
        if self.is_empty():
            raise IndexError("peek з порожньої черги")
        return self.front.data

    def size(self):                                 # повертає кількість елементів у черзі
        return self.count

    def show(self):                                 # виводить усі елементи черги
        current = self.front
        print("Початок черги → ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Кінець\n")

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.show()
print("Перший елемент:", q.peek())
print("Видалено:", q.dequeue())
q.show()
print("Розмір черги:", q.size())