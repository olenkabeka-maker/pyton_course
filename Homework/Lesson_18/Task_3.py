# Task_3
"""Напишіть клас TypeDecorators, який має кілька методів для перетворення результатів функцій до заданого типу (якщо це можливо)"""

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)                                                        # зберігає метадані функції
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Не вдалося перетворити {result!r} у int")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result.lower() in ("true", "1", "yes", "так")
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"Не вдалося перетворити {result!r} у float")
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True

print("Усе працює правильно!")