# Task_1  Method overloading

def animals_talk(animal):
    print(animal.talk())

class Animal:
    def talk():
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'
        
class Cat(Animal):
    def talk (self): 
        return 'meow'

dog =  Dog()
cat = Cat()

animals_talk(dog)
animals_talk(cat)