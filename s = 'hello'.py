s = 'hello'
print(s.count('l'))
print(s.upper())

# method replace   work
text = "Hello World! Hello Python!"
new_text = text.replace("Hello", "Hi")
print(new_text)

# method .split
text = "Hello world, how are you?"
words = text.split('...')
print(words)

#форматування рядків 
name = 'Batman'
super_power = 'intellect'
enemy = 'Joker'
print(f'Superhero name is {name}, his super power - {super_power}, his enemy - {enemy}.')
print(f'Superhero name is {name.upper()}, his super power - {super_power}, his enemy - {enemy}.')
print(f'Superhero name is {name}, his super power - {super_power}, his enemy - {enemy[:3]}.')