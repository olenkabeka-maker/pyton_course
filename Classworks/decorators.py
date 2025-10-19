def decorator(func):
    def wrapper():
        print("Перед виконанням функції")
        func()
        print("Після виконання функції")
    return wrapper

@decorator
def say_hello():
    print("Привіт, Альоно!")

say_hello()  
