# Напишіть декоратор, який виводить функцію з переданими їй аргументами. Треба вивести функцію, а не результат її виконання!

def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))                            # перетворює позиційні аргументи на рядок
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())   # ключові аргументи
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))      # об’єднує все

        print(f"{func.__name__} called with {all_args}")                # виводимо назву функції та аргументи
    return wrapper

@logger                                                                 # те саме, що  add = logger(add)
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)          
square_all(1, 2, 3)  #