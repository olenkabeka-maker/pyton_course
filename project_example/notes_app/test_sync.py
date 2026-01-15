import time
import requests

urls = [
    "http://127.0.0.1:8000/sync/one/",
    "http://127.0.0.1:8000/sync/two/",
    "http://127.0.0.1:8000/sync/three/",
]

start_total = time.time()

for url in urls:
    start = time.time()
    response = requests.get(url)
    duration = time.time() - start
    print(f"{url} → {duration:.2f} сек")

total_duration = time.time() - start_total
print(f"\nЗАГАЛЬНИЙ ЧАС (sync): {total_duration:.2f} сек")