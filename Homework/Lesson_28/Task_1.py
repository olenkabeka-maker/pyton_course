"""Бульбашкове сортування можна модифікувати для "бульбашкового" сортування в обох напрямках. Перший прохід переміщує список "вгору", 
а другий прохід - "вниз". Реалізуйте цей варіант і опишіть, за яких обставин він може бути доцільним."""

"""Cocktail Shaker Sort працює краще, у випадках:
1. Коли список майже відсортований, бо рухає ел-ти в обох напр.
2. Коли дані мають багато елементів "не на своїх місцях" на обох кінцях
3. Для "практичних" невеликих списків."""

def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
                
        for i in range(start, end):                     # прохід зліва направо — "піднімає" найбільші елементи вгору
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:                                 # якщо не було перестановок, масив уже відсортований
            break

        swapped = False
        end -= 1
 
        for i in range(end - 1, start - 1, -1):         # прохід справа наліво — "опускає" найменші елементи вниз
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr
print(cocktail_shaker_sort([5, 3, 1, 4, 2]))