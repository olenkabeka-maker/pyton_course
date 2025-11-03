# Task_3
"""Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax"""

class MyIterable:
    def __init__(self, data):
        self.data = list(data)              # зберігаємо дані у списку

    def __iter__(self):
        return MyIterator(self.data)        # повертаємо ітератор

    def __getitem__(self, index):           # __getitem__() дає доступ через квадратні дужки
        return self.data[index]             # отримуємо елемент за індексом

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

nums = MyIterable([10, 20, 30, 40])

print("Ітерація через for-in:")
for n in nums:
    print(n)

print("\nОтримання елемента за індексом:")
print(nums[0])
print(nums[2])