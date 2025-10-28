# податковий калькулятор CISCO

income = float(input("Введіть річний дохід: "))

if income < 85528:
    tax = income * 0.18 - 556.02

else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0.0:
    tax = 0.0   
    
tax = round(tax, 0)

print("Податок склав:", tax, "талера") 

# високосний рік чи ні

year = int(input("Введіть рік: "))

if year < 1582:
    print("Не в межах григоріанського календарного періоду")

elif year %  4 != 0:
    print("Це звичайний рік")

elif year % 100 != 0 :
    print("Це високосний рік")

elif year % 400 != 0:
    print("Це звичайний рік")

else:
   print("Це високосний рік") 
