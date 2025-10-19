def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):    # Чи всі числа позитивні
        return func1(nums)              # Виконуємо першу функцію
    else:
        return func2(nums)              # Інакше виконуємо другу функцію

# Функції
def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

# твердження
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

# Перевірка (чи працює код правильно)
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print("Усе працює чудово!")