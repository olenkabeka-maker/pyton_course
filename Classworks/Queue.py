# Queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)   # додаємо в кінець

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # видаляємо з початку

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.dequeue())  # A
print(q.dequeue())  # B
print(q.size())     # 1

# 2 example
from collections import deque

queue = deque()

queue.append("A")   # enqueue
queue.append("B")
queue.append("C")

print(queue.popleft())  # dequeue → A
print(queue)            # deque(['B', 'C'])