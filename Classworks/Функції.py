# A tree from ***
def print_tree (n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*', end=' ')
        print()
print_tree(7) 

# функція з дек.аргументами

def sum_of_squares(*args):
    return_value = 0
    for num in args:
        return_value += num**2
    return return_value

print(sum_of_squares(2, 3, 3, 5, 1, 6))

def describe_laptop(brand, color="black"): 
	print(f"Мій ноутбук виготовлено компанією {brand}, а його колір — {color}") 

describe_laptop("Lenovo")

def modulo(a, b):
    return a % b
modulo(9, 5) == modulo(b=5, a=9)