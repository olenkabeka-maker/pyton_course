
    #for 
a_list = [1, 2, 3, 4, 5]
i = 0
while i < len(a_list):
    print(a_list [i])
    i += 1


lista = [1, 2,3, 4, 5, 6, 7]
print(lista[-4:-8:-1])

#        0  1  2  3  4  5  6
lista = [1, 2, 3, 4, 5, 6, 7]

print(lista[3: :-1])

#        0  1  2  3  4  5  6  7
lista = [1, 2, 3, 4, 5, 6, 7, 8]
#       -8 -7 -6 -5 -4 -3 -2 -1
aaa = lista[::-1]
print(aaa)
bbb = aaa[4:]
print(bbb)
print(dir([]))

x = input("просто натисніть Enter")
print(id(x))

import this


temp = []
for i in range(0, 10):
    if i % 2:
        continue
    temp.append(i)
print(sum(temp))
