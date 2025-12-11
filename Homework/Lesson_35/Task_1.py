"""У нас є нижче вхідний список чисел, деякі з яких є простими. Потрібно створити функцію, яка приймає на вхід число 
та повертає логічне значення, незалежно від того, просте воно чи ні. Використовуйте ThreadPoolExecutor та ProcessPoolExecutor 
для створення різних одночасних реалізацій фільтрації ЧИСЕЛ."""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

ЧИСЛА = [ 
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

def is_prime(n: int) -> bool:           #  функція визначення простого числа
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def run_threads(nums):                  #  запуск у ThreadPoolExecutor
    start = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, nums))
    duration = time.time() - start
    return results, duration


def run_processes(nums):                #  запуск у ProcessPoolExecutor
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, nums))
    duration = time.time() - start
    return results, duration

if __name__ == "__main__":
    
    thread_result, thread_time = run_threads(ЧИСЛА)     

    process_result, process_time = run_processes(ЧИСЛА)

    print("Результат ThreadPoolExecutor:", thread_result)
    print("Час виконання:", thread_time, "сек\n")

    print("Результат ProcessPoolExecutor:", process_result)
    print("Час виконання:", process_time, "сек\n")

    print("--- Висновок ---")
    if thread_time < process_time:
        print("Threads швидші")
    else:
        print("Processes швидші")