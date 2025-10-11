#TASK 1
#held
string = 'helloworld'
print(string[0:2] + string[-2:len(string)])

#mymy
string = 'my'
print(string[0:2] + string[0:2])

#Emty String
string = 'x'
print(string[0:2] + string[0:2])
if len(string) < 2:
    print('Emty String')

#TASK 2
phone_number = '0661192261'
if len(phone_number) == 10:
    print("Number is correct.")
elif phone_number.isdigit():
    print("Number is correct.")
else:
    print("Number is wrong!")

#TASK 3
a = 5
b = 4
expression = input(f"Скільки буде {a} + {b}?")
if expression == str(a + b):
    print("Вірно!!!")
else:
    print(f"Невірно. Правильна відповідь: {a + b}")

#TASK 4
my_name = "альона"
user_name = input("Введіть ваше ім'я: ")
if user_name.lower() == my_name:
    print(True)
else:
    print(False)