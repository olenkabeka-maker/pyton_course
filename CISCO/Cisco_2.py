n = int(input("ВВедіть значення n: "))

print(n >= 100)

number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))
 
largest_number = number1
 
if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3
    
print("Найбільше число це:", largest_number)


number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))

largest_number = max(number1, number2, number3)
 
print("Найбільше число це:", largest_number)

