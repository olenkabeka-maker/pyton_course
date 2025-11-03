# Ітератори

for number in [1, 2, 3]:
    print(number)

iterator = iter([1, 2, 3])
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break   


# Create an iterator which would iterate over items randomly number of iterations should be equal to number of elements 
 # elements should not be repeated

import random

class RandomIterator:
    def __init__(self, data):
        self.data = list(data)
        self.indices = list(range(len(self.data)))
        random.shuffle(self.indices)                    # перемішуємо індекси
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        index = self.indices[self.position]
        self.position += 1
        return self.data[index]

items = [17, 24, 37, 47, 56]
it = RandomIterator(items)

for x in it:
    print(x)