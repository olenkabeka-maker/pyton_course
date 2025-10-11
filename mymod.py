# TASK 3 Home work 9

def count_lines(name):
    """Підраховує кількість рядків модуля"""
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines)

def count_chars(name):
    """Підраховує кількість символів модуля"""
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text)

def test(name):
    """Викликає обидві функції та виводить результати"""
    num_lines = count_lines(name)
    num_chars = count_chars(name)
    print(f"Файл '{name}' містить {num_lines} рядків та {num_chars} символів.")