# All tasks should be solved using recursion

#  Task 1

from typing import Union

def to_power(x: Union[int, float], exp: int) -> Union[int, float]:      # exp — цілий показник степеня

    if exp < 0:                         # якщо exp менше нуля - помилка
        raise ValueError("This function works only with exp > 0.")

    if exp == 0:                        # базовий випадок
        return 1

    return x * to_power(x, exp - 1)

result = to_power(2, 3)
print(result)
result = to_power(3.5, 2)
print(result)


#  Task 2

def is_palindrome(looking_str: str, index: int = 0) -> bool:    # index - позиція символів в слові
    if index >= len(looking_str) // 2:                          # перший базовий випадок
        return True

    if looking_str[index] != looking_str[-(index + 1)]:         # другий базовий випадок (помилка)
        return False

    return is_palindrome(looking_str, index + 1)

print(is_palindrome("mom"))      
print(is_palindrome("sassas"))   
print(is_palindrome("o"))