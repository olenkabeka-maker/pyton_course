# створюємо функцію для послідовності Fibonacci

def fib(n):
    a, b = 0, 1 
    for i in range(n):
        a, b = b, a+b
    return a
print(fib(int(input("What fib do you whant?: "))))

# отримуємо доступ до функції fibonacci

from fibonacci import fib

# АБО

import fibonacci
fibonacci.fib(2)

