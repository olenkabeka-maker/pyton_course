# Напишіть декоратор 'arg_rules', який перевіряє аргументи, передані ф-ції.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            
            if not isinstance(arg, type_):                              # Перевірка типу
                print(f"Argument must be of type {type_.__name__}")
                return False
           
            if len(arg) > max_length:                                   # Перевірка довжини
                print(f"Argument length must be <= {max_length}")
                return False

            for symbol in contains:                                     # Перевірка на наявність усіх символів/рядків 
                if symbol not in arg:
                    print(f"Argument must contain '{symbol}'")
                    return False

            return func(arg)                                            # коли всі перевіркм пройдено
        return wrapper
    return decorator

# Приклад використання

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# Перевірка 
assert create_slogan('johndoe05@gmail.com') is False                            # якщо надто довго
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

# Перевірка виводу
print(create_slogan('S@SH05'))
print(create_slogan('johndoe05@gmail.com'))