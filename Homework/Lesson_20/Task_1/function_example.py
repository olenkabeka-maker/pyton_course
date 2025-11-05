def a_b(a, b):
    
    try:
        a = float(a)
        b = float(b)
        result = a ** 2 / b
        return result
    except ValueError:
        return "Помилка! Вводь лише числа!"
    except ZeroDivisionError:
        return "Не можна ділити на нуль!"