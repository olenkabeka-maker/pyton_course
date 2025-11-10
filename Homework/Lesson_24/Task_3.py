# Task_3
"""Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. 
Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - 
raise ValueError with proper info Message"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        
        temp_stack = Stack()                    # пошук елемента e у стеку з збереженням порядку
        found = None

        while not self.is_empty():              # переносить елементи у тимчасовий стек, шукаючи потрібний
            item = self.pop()
            if item == e:
                found = item
                break
            else:
                temp_stack.push(item)
        
        while not temp_stack.is_empty():        # повертає назад усі елементи, щоб порядок зберігся
            self.push(temp_stack.pop())

        if found is not None:
            return found
        else:
            raise ValueError(f"Element '{e}' not found in stack")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Стек перед пошуком:", s.items)

try:
    found = s.get_from_stack(30)
    print("Знайдено елемент:", found)
except ValueError as err:
    print(err)

print("Стек після пошуку:", s.items)