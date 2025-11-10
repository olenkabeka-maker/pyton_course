# Task_1    Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack

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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_string(input_string):           # функція для реверсу рядка
    stack = Stack()

    for ch in input_string:                 # додає усі символи у стек
        stack.push(ch)
    
    reversed_str = ""                       # виймає символи у зворотному порядку
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

if __name__ == "__main__":
    text = input("Введіть символи: ")
    reversed_text = reverse_string(text)
    print("Результат навпвки:", reversed_text)