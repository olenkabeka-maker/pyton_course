
def outer_function(msg):                    # Зовнішня функція
    print("Я - зовнішня функція!")

    def inner_function():                   # Внутрішня функція
        print("Я - внутрішня функція!")
        print("Повідомлення:", msg)
    
    return inner_function                   # Повертає внутрішню функцію

my_func = outer_function("Привіт, Альоно!")  # Викликає зовн. функц. та отримання внутрішн.

my_func()                                   # Виклик внутрішн. функції


#через lambda

def outer(msg):
    return lambda: print(f"Я внутрішня функція працюю! Повідомлення: {msg}")

inner_func = outer("Привіт, Альоно!")       # Виклик зовнішньої функції і збереження внутрішньої

inner_func()                                # Виклик внутрішньої функції