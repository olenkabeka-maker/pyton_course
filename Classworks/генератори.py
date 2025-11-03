def createGenerator():
   print("Beginning of generator")
   for i in range(3):
      yield i
   print("After yield")
print("Before assignment")
my_generator = createGenerator()
print("After assignment")
for i in my_generator:
   print(i)