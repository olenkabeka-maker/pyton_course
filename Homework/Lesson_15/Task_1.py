# Task_1    клас під назвою Person

class Person():
    def __init__ (self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        self.greeting = greeting
message = Person('Carl', 'Johnson', 26)
print(f"Hello, my name is {message.firstname} {message.lastname} and I'm {message.age} years old.")