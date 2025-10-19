# Function as objects of the 1st class

def add_five(x):
    return x+5

def do_twice(f):
    def resulting_func(x):
        return f(f(x))
    return resulting_func

result = do_twice(add_five)  
print(result(3))      


class Adder:
    def __init__(self, n):
        self.n = n 
    def __call__(self, x):
        return self.n+x 
x = Adder(10)
print(x(10))

def sqr(item):
    return item **2
print(sqr(2))


from functools import partial
def multiply_two_numbers(a, b):
    print(a, b)
    return a*b 

multiply_numbers_two = partial(multiply_two_numbers, 2)

def multiply_numbers_two(b):
    return multiply_two_numbers(2, b)
print(multiply_numbers_two(10))