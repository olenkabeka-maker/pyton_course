# TASK 1
# створення функції favorite_movie

#1st version
def favorite_movie(movie):
    print("My favorite movie is named" + ' ' + movie)

favorite_movie('"Friends"')

#2nd version
def favorite_movie(movie):
    print(f"My favorite movie is named {movie}")

favorite_movie('"Friends"')

#TASK 2
#функція зі словником у середині

def make_country(name, capital):
    country = {"name": name, "capital": capital}
    print(country)
    return country
make_country("Ukraine", "Kyiv")
make_country("Spain", "Madryd")

# TASK 3
# a simple calculator

def make_operation(operator, *args):
    if operator == '+':
        result = 0
        for num in args:
            result += num
        return result
    
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result 

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))