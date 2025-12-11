"""Завантажте всі коментарі з https://jsonplaceholder.typicode.com/. В результаті, зберігайте всі коментарі в хронологічному порядку в JSON 
та виводьте їх у файл. Для цього завдання використовуйте бібліотеки для паралельної та багатопроцесорної обробки запитів до Reddit API."""

import json
import math
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

BASE_URL = "https://jsonplaceholder.typicode.com/comments"
OUTPUT_FILE = "comments.json"


def fetch_comments(ids):                                        # завантаження коментарів за списком ID
    comments = []
    for cid in ids:
        url = f"{BASE_URL}/{cid}"
        response = requests.get(url)
        if response.status_code == 200:
            comments.append(response.json())
    return comments


def split_ids(total, parts):                                    # поділ ID на частини для паралельного запуску
    size = math.ceil(total / parts)
    return [list(range(i, min(i + size, total)))
            for i in range(1, total + 1, size)]


def load_with_threads(total_ids, workers=10):                   # паралельне завантаження (Threads)
    id_batches = split_ids(total_ids, workers)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(fetch_comments, id_batches)

    comments = [c for batch in results for c in batch]
    return sorted(comments, key=lambda x: x['id'])


def load_with_processes(total_ids, workers=6):                  # паралельне завантаження (Processes)
    id_batches = split_ids(total_ids, workers)

    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = executor.map(fetch_comments, id_batches)

    comments = [c for batch in results for c in batch]
    return sorted(comments, key=lambda x: x['id'])


if __name__ == "__main__":                                      # запуск
    TOTAL = 500                                                 # у JSONPlaceholder рівно 500 коментарів

    comments_threads = load_with_threads(TOTAL)

    comments_processes = load_with_processes(TOTAL)

    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:         # запис у файл результатів з потоків
        json.dump(comments_threads, f, indent=2, ensure_ascii=False)

    print("Файл comments.json створено!")
    print("Завантажено коментарів:", len(comments_threads))