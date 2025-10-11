def calculate_average(numbers):
    sum = 0
    for num in numbers:
     sum += num
    average = sum (len(numbers))
    return average

# Example 2: Naming Conventions
class UserAccount:
    def __init__(self, UserName, Email, Age):
        self.UserName = UserName
        self.Email = Email
        self.Age = Age
    
    def display_INFO(self):
        print(f"User: {self.UserName}, Email: {self.Email}, Age: {self.Age}")

# Example 3: Imports and Module Level Dunder Names
import os,sys
import numpy as np
from datetime import datetime, date, time
__version__ = '1.0.0'
__author__ = "John Doe"

# Example 4: Maximum Line Length and Line Breaks
def process_data(data, filter_condition, transform_function, output_format, debug_mode=False, log_file='process.log', max_iterations=1000):
    # Process the data here
    pass

# Example 5: Comments and Docstrings
#this function calculates the factorial of a number
def factorial(n):
    """Calculate factorial"""
    if n == 0: return 1
    else: return n * factorial(n - 1)

# Example 6: Compound Statements
if x == 5: print("x is 5"); y = 10

# Example 7: Whitespace in Expressions and Statements
x=[1,2,3,4,5]
y= x[0] *2+3

# Example 8: Long Line String Formatting
long_string = "This is a very long string that exceeds the recommended maximum line length of 79 characters in PEP 8. It should be formatted properly."

# Example 9: Extra Spaces
def greet( name ):
    print( "Hello, " + name + "!" )

# Example 10: Variable Naming Conventions
firstName = "John"
LastName = "Doe"
AGE = 30
*private*var = "This is a private variable"

# Example 11: Class Naming Conventions
class customer_data:
    pass
class HTTPClient:
    pass

# Example 12: Function Naming Conventions
def Calculate_Total(items):
    pass
def fetch_Data_From_API():
    pass

# Example 13: Constant Naming Conventions
pi = 3.14159
MAX_CONNECTIONS = 100
default_timeout = 30
SECONDS_IN_A_DAY = 24 * 60 * 60
                    