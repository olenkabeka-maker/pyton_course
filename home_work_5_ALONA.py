# TASK 1
# Гра "Вгадай число" число від 1 до 10
import random

secret_number = random.randint(1, 10)
user_guess = int(input("Вгадай число від 1 до 10: "))
if user_guess == secret_number:
    print("Вітаю! Ти вгадав!")
else:
    print(f"Ти не вгадав. Загадане число було {secret_number}. Спробуй ще.")

#TASK 2

user_name = input("Please write name: ")
age = input("How old are you? ")
print("Hello," + " " + str(user_name) + "," + " " + "on your next birthday you'll be" + " "  + str(age) + "+1 years")

#TASK 3
import random

user_input = input("Введіть рядок: ")
num_random_strings = 5
for _ in range(num_random_strings):
    random_string = ''.join(random.choice(user_input) for _ in range(len(user_input)))
    print(random_string)