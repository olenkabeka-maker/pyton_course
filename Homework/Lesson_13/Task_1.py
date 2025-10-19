# функція, яка повертає кількість локальних змінних у функції func

def count_local_vars(func):

    return func.__code__.co_nlocals     # .co_nlocals  показ. кільк. локальн. змін. у ф-ції; func.__code__ — об’єкт з байт-кодом ф-ії.

def example():    # Приклад функції
    a = 10
    b = 20
    c = a + b
    return c

print("Кількість локальних змінних у 'example':", count_local_vars(example))