
    #for 
a_list = [1, 2, 3, 4, 5]
i = 0
while i < len(a_list):
    print(a_list [i])
    i += 1

a_list = [1, 2, 3, 4, 5]
for item in a_list:
    print(item)

a_list = [1, 2, 3, 4]
for i in range(len(a_list)):
    print(a_list[i])

a_list = [1, 2, 3, 4, 5]
for item in a_list:
    if item == 4:
        break
    print(item)
else:
    print("OK!")

print(True is True)

x = 10
if x < 5:
	print(10 + 10)
elif x > 5:
	print(101 - 202)
elif x == 10:
	print(1/0)
else:
	print(1 * 10)



n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue
print(n)