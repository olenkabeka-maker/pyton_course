class Car():
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color 
        self.total_driven_km = 0
    def repaint(self, color):
        self.color = color
    def drive(self, km_driven):
        self.total_driven_km += km_driven
my_car = Car('Volvo', 'v90', 2017, 'black')
print(my_car.color)
my_car.repaint('green')
print(my_car.color)
print(my_car.total_driven_km)
my_car.drive(1000)
print(my_car.total_driven_km)

#2 cars

class Car():
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color 
        self.total_driven_km = 0
    def repaint(self, color):
        self.color = color
    def drive(self, km_driven):
        self.total_driven_km += km_driven

car1 = Car('Volvo', 'v90', 2016, 'white')
car2 = Car('Ford', 'Focus', 2014, 'grey')
print('car1 is of brand ' + car1.brand)
print('car2 is of brand ' + car2.brand)

# how many cars

class Car():

    total_numberof_cars = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color 
        self.total_driven_km = 0
        Car.total_numberof_cars += 1

    def repaint(self, color):
        self.color = color
    def drive(self, km_driven):
        self.total_driven_km += km_driven

car1 = Car('Volvo', 'v90', 2016, 'white')
print(Car.total_numberof_cars)
car2 = Car('Ford', 'Focus', 2014, 'grey')
print(Car.total_numberof_cars)