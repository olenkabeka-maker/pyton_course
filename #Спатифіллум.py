#Спатифіллум

plant = input("Enter the name of the plant: ")

if plant == 'Spathiphyllum':
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")

#податки
income = float(input("Введіть річний дохід: "))

if income < 85528:
 tax = income * 0.18 - 556.02
# тут записуємо ваш код.

tax = round(tax, 0)
print("Податок склав:", tax, "талера") 
 
