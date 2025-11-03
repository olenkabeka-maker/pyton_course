# Task_2
""" Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
'start', 'end', and optional step.          Tips: See the documentation for 'range' function"""

def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step == 0:                               # щоб не було нескінченного циклу
        raise ValueError("step cannot be 0")
   
    if step > 0:                                # логіка генерації чисел
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

print(list(in_range(6)))         
print(list(in_range(2, 7)))      
print(list(in_range(10, 2, -2)))
print(list(in_range(10, 22, 3)))