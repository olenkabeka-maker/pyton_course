"""Створіть окремий асинхронний код для обчислення чисел Фібоначчі, факторіала, квадратів та кубічних чисел для вхідного числа. 
Заплануйте виконання цього коду за допомогою asyncio.gather для списку цілих чисел від 1 до 10. Вам потрібно отримати чотири списки 
результатів з відповідних функцій."""

import asyncio
import time

def fibonacci(n):                               # обчислювальні функції
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def square(n):
    return n * n

def cube(n):
    return n * n * n

async def async_fibonacci(n):                   # aсинхронні функції
    return fibonacci(n)

async def async_factorial(n):
    return factorial(n)

async def async_square(n):
    return square(n)

async def async_cube(n):
    return cube(n)


async def main():
    numbers = list(range(1, 11))

    start = time.time()

    fib_results = await asyncio.gather(*(async_fibonacci(n) for n in numbers))
    fact_results = await asyncio.gather(*(async_factorial(n) for n in numbers))
    square_results = await asyncio.gather(*(async_square(n) for n in numbers))
    cube_results = await asyncio.gather(*(async_cube(n) for n in numbers))

    end = time.time()

    print("=== ASYNCIO RESULTS ===")
    print("Fibonacci:", fib_results)
    print("Factorial:", fact_results)
    print("Squares:", square_results)
    print("Cubes:", cube_results)
    print(f"Asyncio time: {end - start:.4f} sec")

asyncio.run(main())

"""Перепишіть код, щоб використовувати прості функції для отримання тих самих результатів, але з 
використанням багатопроцесорної бібліотеки. Засічіть час виконання обох реалізацій."""

import multiprocessing
import time


def fibonacci(n):                               # ті самі обчислювальні функції
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def square(n):
    return n * n

def cube(n):
    return n * n * n


def run_multiprocessing():
    numbers = list(range(1, 11))
    start = time.time()

    with multiprocessing.Pool() as pool:
        fib_results = pool.map(fibonacci, numbers)
        fact_results = pool.map(factorial, numbers)
        square_results = pool.map(square, numbers)
        cube_results = pool.map(cube, numbers)

    end = time.time()

    print("\n=== MULTIPROCESSING RESULTS ===")
    print("Fibonacci:", fib_results)
    print("Factorial:", fact_results)
    print("Squares:", square_results)
    print("Cubes:", cube_results)
    print(f"Multiprocessing time: {end - start:.4f} sec")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")  
    run_multiprocessing()