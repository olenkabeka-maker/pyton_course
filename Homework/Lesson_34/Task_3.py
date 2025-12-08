"""Завантажте всі коментарі з https://jsonplaceholder.typicode.com/ В результаті, зберігайте всі коментарі в хронологічному порядку 
в JSON та виводьте їх у файл. Для цього завдання використовуйте Threads для здійснення запитів до API Reddit"""

import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://jsonplaceholder.typicode.com/comments"
TOTAL_COMMENTS = 500                                                # Загальна кількість коментарів
MAX_THREADS = 20                                                    # Максимальна кількість одночасних потоків

def fetch_comment(comment_id):
    url = f"{BASE_URL}/{comment_id}"                                # Завантажує коментар за id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Помилка при завантаженні коментаря {comment_id}: {response.status_code}")
        return None

def main():
    comments = []
   
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:   # Використовує ThreadPoolExecutor для обмеженої кількості потоків
        futures = [executor.submit(fetch_comment, i) for i in range(1, TOTAL_COMMENTS + 1)] # Створюємо задачі для всіх коментарів

        for future in as_completed(futures):                        # Обробляє результати по готовності
            result = future.result()
            if result:
                comments.append(result)
    
    comments_sorted = sorted(comments, key=lambda x: x['id'])       # Сортує коментарі за id (хронологічно)
    
    with open("comments.json", "w", encoding="utf-8") as f:         # Зберігаємо у JSON файл
        json.dump(comments_sorted, f, ensure_ascii=False, indent=4)

    print(f"Завантажено та збережено {len(comments_sorted)} коментарів у файл comments.json")

if __name__ == "__main__":
    main()