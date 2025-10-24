# Task_2   class Mathematician

class Mathematician:
    def square_nums(self, numbers):              #Повертає список чисел у квадраті
        return [n ** 2 for n in numbers]

    def remove_positives(self, numbers):        #Повертає список без додатних чисел
        return [n for n in numbers if n <= 0]

    def filter_leaps(self, years):              # Повертає високосні роки 
       
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("Всі тести пройдено успішно!")