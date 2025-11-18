"""Реалізуйте функцію mergeSort без використання оператора зрізу"""

def merge_sort(arr):
    temp = [0] * len(arr)
    _merge_sort(arr, temp, 0, len(arr) - 1)

def _merge_sort(arr, temp, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    _merge_sort(arr, temp, left, mid)
    _merge_sort(arr, temp, mid + 1, right)
    merge(arr, temp, left, mid, right)


def merge(arr, temp, left, mid, right):
    i = left                                # початок лівої частини
    j = mid + 1                             # початок правої частини
    k = left                                # позиція у тимчасовому масиві

    while i <= mid and j <= right:          # основне об'єднання
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:                         # додаю залишок лівої частини
        temp[k] = arr[i]
        i += 1
        k += 1

    
    while j <= right:                       # додаю залишок правої частини
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for idx in range(left, right + 1):      # переписую назад у основний масив
        arr[idx] = temp[idx]

arr = [5, 2, 4, 6, 1, 3]
merge_sort(arr)
print(arr)
