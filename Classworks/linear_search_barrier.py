def linear_search_barrier(arr, x):
    n = len(arr)
    arr.append(x)               # додаємо бар’єр
    i = 0

    while arr[i] != x:
        i += 1

    arr.pop()                   # видаляємо бар’єр

    if i < n:
        return i                # індекс знайденого елемента
    else:
        return -1               # не знайдено


arr = [3, 5, 8, 2, 9]
x = 2

result = linear_search_barrier(arr, x)

if result != -1:
    print(f"Елемент {x} знайдено на позиції {result}")
else:
    print(f"Елемент {x} не знайдено")