"""Реалізуйте стек за допомогою однозв'язного списку"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None                             # посилання на вершину стека
        self.count = 0                              # кількість елементів

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)                       # додає елемент у стек (на верхівку)
        new_node.next = self.top                    # новий вузол посилається на попередній "верх"
        self.top = new_node                         # тепер вершина — це новий вузол
        self.count += 1

    def pop(self):
        if self.is_empty():                         # видаляє верхній елемент і повертає його
            raise IndexError("pop з порожнього стека")

        data = self.top.data
        self.top = self.top.next                    # пересуває вершину вниз
        self.count -= 1
        return data

    def peek(self):
        if self.is_empty():                         # повертає верхній елемент без видалення
            raise IndexError("peek з порожнього стека")
        return self.top.data

    def size(self):                                 # повертає кількість елементів
        return self.count

    def show(self):                                 # виводить елементи стека
        current = self.top
        print("Верх стека ↓")
        while current:
            print(current.data)
            current = current.next
        print("Кінець стека\n")


stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")
stack.show()

print("Верхній елемент:", stack.peek())
print("Видалено:", stack.pop())
stack.show()
print("Розмір стека:", stack.size())