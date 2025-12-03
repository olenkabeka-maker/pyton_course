# Task_2
"""Завантажте всі коментарі https://jsonplaceholder.typicode.com/ В результаті, 
зберігайте всі коментарі в хронологічному порядку в JSON та виводьте їх у файл"""

import requests
import json

url = "https://jsonplaceholder.typicode.com/comments"       # завантажую всі коментарі
response = requests.get(url)

comments = response.json()                                  # перетворюю на Python-список

comments_sorted = sorted(comments, key=lambda x: x["id"])   # сортую хронологічно за id

output_file = "comments_sorted.json"                        # зберігаю у файл JSON

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(comments_sorted, f, ensure_ascii=False, indent=4)

print(f"Готово! Коментарі збережено у {output_file}")