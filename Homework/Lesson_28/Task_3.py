"""Перереалізуйте швидке сортування, використавши сортування вставками для списків малої довжинита, 
використовуйте його для сортування випадкового списку цілих чисел."""

import random

def insertion_sort(arr, left, right):                   # сортування вставками
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, left, right, threshold=10):          # швидке сортування з порогом
    while left < right:

        if right - left + 1 <= threshold:               # якщо підмасив маленький — вставки
            insertion_sort(arr, left, right)
            return
        
        pivot = arr[(left + right) // 2]                # вибір опорного елемента

        i, j = left, right
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        if (j - left) < (right - i):                    # рекурсія на меншу частину, перехід на більшу
            quicksort(arr, left, j, threshold)
            left = i
        else:
            quicksort(arr, i, right, threshold)
            right = j


lst = [random.randint(0, 10000) for _ in range(30)]     # випадковий список

print("Початковий список:")
print(lst)

quicksort(lst, 0, len(lst) - 1)                         # сортування

print("\nВідсортований список:")
print(lst)