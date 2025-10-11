# LAB 1
a = float(input("Введіть перше значення: "))
b = float(input("Введіть друге значення: "))

print('a + b = ' + str(a+b))
print('a - b = ' + str(a-b))
print('a * b = ' + str(a*b))
print('a / b = ' + str(a/b))

print("\nУсе, друзі!")

#LAB 2
x = float(input("Введіть значення x: "))
y = 1. / (x + 1. / (x + 1. / (x + 1. / x)))

print("y =", y)

#LAB 3

hour = int(input("Час початку (години): "))
mins = int(input("Час початку (хвилини): "))
dura = int(input("Тривалість події (хвилин): "))

mins = mins + dura           # знаходимо суму всіх хвилин
hour = hour + mins // 60     # знаходимо кількість годин, прихованих у хвилинах, та оновлюємо час
mins = mins % 60             # коригуємо хвилини, щоб вони потрапляли в діапазон (0..59)
hour = hour % 24             # коригуємо години, щоб вони потрапляли в діапазон (0..23)

print(hour, ":", mins, sep='')

z=y=x=1
print(x,y,z, sep='*')