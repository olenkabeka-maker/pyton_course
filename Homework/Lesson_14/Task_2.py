# Напишіть декоратор, який приймає список стоп-слів та замінює їх на * всередині декорованої функції.

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)          # викликаємо оригінальну функцію
            for word in words:
                result = result.replace(word, "*")  # замінюємо кожне стоп-слово на "*"
            return result
        return wrapper
    return decorator

# використовуємо

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# перевірка

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))