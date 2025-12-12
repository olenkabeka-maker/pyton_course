"""Завантажте всі коментарі з https://jsonplaceholder.typicode.com/ . В результаті, зберігайте всі коментарі в хронологічному порядку в JSON 
та виводьте їх у файл. Використовуйте бібліотеки asyncio та aiohttp для здійснення запитів в APi"""


import asyncio
import aiohttp
import json

URL = "https://jsonplaceholder.typicode.com/comments"


async def fetch_comments(session):
    async with session.get(URL) as response:                            # завантажую всі коментарі одним запитом
        response.raise_for_status()
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        print("Завантаження коментарів...")

        comments = await fetch_comments(session)

        
        comments_sorted = sorted(comments, key=lambda c: c["id"])       # сортую за id (хронологічний порядок)

        
        with open("comments.json", "w", encoding="utf-8") as file:      # запис у файл
            json.dump(comments_sorted, file, indent=4, ensure_ascii=False)

        print(f"Збережено {len(comments_sorted)} коментарів у файл comments.json")


if __name__ == "__main__":
    asyncio.run(main())