# Task_1  
"""Create your own implementation of a built-in function enumerate, named 'with_index', which takes 
two parameters: 'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function"""

def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item                           # на кожній ітерації повертає кортеж (index, item)
        index += 1

for i, val in with_index(['a', 'b', 'c'], start=1):
    print(i, val)