#TASK
def a_b():
    try:
        a = float(input("ВВедіть значення a: "))
        b = float(input("ВВедіть значення b: "))
        result = a ** 2/ b
        print("Результат: ", result)

    except ValueError:
        print("Помилка! Вводь лише числа!")

    except ZeroDivisionError:
        print("Не можна ділити на нуль!")

a_b()