#TASK 1 Найбільше число з рандомних
import random
numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(1, 100))
    i += 1
print("Список чисел:", numbers)
max_num = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1
print("Найбільше число:", max_num)

#TASK 2 Ексклюзивні номери

import random

#перший список
list_1 = []
i = 0
while i < 10:
    list_1.append(random.randint(1, 10))
    i += 1

#другий список
list_2 = []
i = 0
while i < 10:
    list_2.append(random.randint(1, 10))
    i += 1

#третій список
shared_list = []
i = 0
while i < len(list_1):
    if list_1[i] in list_2 and list_1[i] not in shared_list:
        shared_list.append(list_1[i])
    i += 1
print("Список 1:", list_1)
print("Список 2:", list_2)
print("Спільний список:", shared_list)

#TASK 3 Вилучення чисел, які діляться на 7, але не на 5

#список від 1 до 100
numbers = []
i = 1
while i <= 100:
    numbers.append(i)
    i += 1

#числа, що діляться на 7, але!! не на 5
result = []
i = 0
while i < len(numbers):
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        result.append(numbers[i])
    i += 1
print("Числа, що діляться на 7, але не на 5:", result)