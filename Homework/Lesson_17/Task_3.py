# Task_3    Fraction

from math import gcd

class Fraction:
      
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both numerator and denominator must be integers.")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        common = gcd(numerator, denominator)                                    # скорочення дробу
        self.numerator = numerator // common
        self.denominator = denominator // common

        if self.denominator < 0:                                                # якщо знаменник від’ємний — переносимо знак у чисельник
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __eq__(self, other):                                                            # порівняння
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":                                          # приклад
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    print(x + y)      
    print(x - y)     
    print(x * y)      
    print(x / y)          
    print(x == Fraction(2, 4))
    print(x > y)