#TASK 1  Створення програми
 
sentence = input("Введіть речення: ")
words = sentence.split()
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

#TASK 2 

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_prices = {}
for item in stock:
    total_prices[item] = stock[item] * prices[item]
print(total_prices)

#TASK 3 Cтворити список кортежів (i, j), де j = i**2
result = [(i, i**2) for i in range(1, 11)]
print(result)

#TASK 4 Робимо список днів тижня
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_dict = {i+1: day for i, day in enumerate(days)}    # Створення словника
reverse_day_dict = {day: i+1 for i, day in enumerate(days)}  #навпаки
print(day_dict)
print(reverse_day_dict)