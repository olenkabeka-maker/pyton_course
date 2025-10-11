#lists/tuples
our_fist_list = [1, 2, 3]
another = [1, '1', 3.0]

our_fist_tuple = (1, 2, 3)
another_tuple = (1, '1', 3.0)

x = 1
y = 'c'

print(x in our_fist_tuple)
print(y in another)
print(x not in another_tuple)

#методи в списках
l = [1, 2, 3, 4]
l.append(5)
print(l)

l.extend([6, 7])
print(l)
l.pop()
print(l)

l.insert(0, 1)
print(l)

r = range(10)
print(r[0])
print(list(r[1:5]))


for i in range(0, 11, 2):
    print(i)

s = {1, 2, 3, 4}
for it in s:
    print(it)