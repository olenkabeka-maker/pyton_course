# Task_2  клас Dog з атрибутом класу 'age_factor'

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age   

    def human_age(self):
        return self.age * Dog.age_factor   

# приклад
dog1 = Dog(8)
print(f"Якби собака була людиною, їй було б {dog1.human_age()} років.")