# Task_2  
"""Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, 
and curly brackets are "balanced." """

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


def is_balanced(expression):
    stack = Stack()
    brackets = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != brackets[ch]:
                return False

    return stack.is_empty()

if __name__ == "__main__":
    text = input("Введіть послідовність символів: ")
    if is_balanced(text):
        print("Дужки збалансовані))")
    else:
        print("Дужки незбалансовані((")