# practise type annotations

"""Go to your implementation of the Phonebook application from module 1 and annotate this code with type hints, 
using knowledge from this lesson."""

import json
import sys
import os
from typing import TypedDict, List, Dict

# ===== Типи даних =====

class PhoneEntry(TypedDict):
    name: str
    lastName: str
    phone: str
    city: str


PhoneBook = Dict[str, List[PhoneEntry]]


# ===== Робота з файлом =====

def load_phonebook(filename: str) -> PhoneBook:
    if not os.path.exists(filename):
        print(f"Помилка: файл {filename} не знайдено!")
        sys.exit(1)

    with open(filename, 'r', encoding='utf-8') as f:
        data: PhoneBook = json.load(f)

    return data


def save_phonebook(filename: str, data: PhoneBook) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Дані збережено!")


# ===== CRUD операції =====

def add_entry(phonebook: PhoneBook) -> None:
    print("\n=== Додавання нового запису ===")
    name: str = input("Введіть ім'я: ")
    last_name: str = input("Введіть прізвище: ")
    phone: str = input("Введіть телефон: ")
    city: str = input("Введіть місто: ")

    new_entry: PhoneEntry = {
        "name": name,
        "lastName": last_name,
        "phone": phone,
        "city": city
    }

    phonebook["phones"].append(new_entry)
    print("Запис додано!")


def search_by_first_name(phonebook: PhoneBook) -> None:
    name: str = input("Введіть ім'я для пошуку: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["name"].lower() == name.lower()
    ]

    _print_results(results)


def search_by_last_name(phonebook: PhoneBook) -> None:
    last_name: str = input("Введіть прізвище для пошуку: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["lastName"].lower() == last_name.lower()
    ]

    _print_results(results)


def search_by_full_name(phonebook: PhoneBook) -> None:
    name: str = input("Введіть ім'я: ")
    last_name: str = input("Введіть прізвище: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["name"].lower() == name.lower()
        and p["lastName"].lower() == last_name.lower()
    ]

    _print_results(results)


def search_by_phone(phonebook: PhoneBook) -> None:
    phone: str = input("Введіть телефон для пошуку: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["phone"] == phone
    ]

    _print_results(results)


def search_by_city(phonebook: PhoneBook) -> None:
    city: str = input("Введіть місто для пошуку: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["city"].lower() == city.lower()
    ]

    _print_results(results)


def delete_by_phone(phonebook: PhoneBook) -> None:
    phone: str = input("Введіть телефон для видалення: ")

    results: List[PhoneEntry] = [
        p for p in phonebook["phones"]
        if p["phone"] == phone
    ]

    if not results:
        print("Запис не знайдено.")
        return

    confirm: str = input("Видалити цей запис? (y/n): ")
    if confirm.lower() == "y":
        phonebook["phones"] = [
            p for p in phonebook["phones"]
            if p["phone"] != phone
        ]
        print("Запис видалено.")
    else:
        print("Видалення скасовано.")


def update_by_phone(phonebook: PhoneBook) -> None:
    phone: str = input("Введіть телефон для оновлення: ")

    for p in phonebook["phones"]:
        if p["phone"] == phone:
            print(f"Знайдено: {p['name']} {p['lastName']} ({p['city']})")

            p["name"] = input(f"Нове ім'я [{p['name']}]: ") or p["name"]
            p["lastName"] = input(f"Нове прізвище [{p['lastName']}]: ") or p["lastName"]
            p["phone"] = input(f"Новий телефон [{p['phone']}]: ") or p["phone"]
            p["city"] = input(f"Нове місто [{p['city']}]: ") or p["city"]

            print("♻️ Запис оновлено.")
            return

    print("Запис не знайдено.")


# ===== Допоміжні =====

def _print_results(results: List[PhoneEntry]) -> None:
    if not results:
        print("Нічого не знайдено.")
        return

    print(f"\nЗнайдено {len(results)} запис(ів):")
    for r in results:
        print(f"{r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")


def show_menu() -> None:
    print("\n===== ТЕЛЕФОННА КНИГА =====")
    print("1. Додати запис")
    print("2. Пошук за ім'ям")
    print("3. Пошук за прізвищем")
    print("4. Пошук за повним ім'ям")
    print("5. Пошук за телефоном")
    print("6. Пошук за містом")
    print("7. Видалити запис")
    print("8. Оновити запис")
    print("9. Вихід")
    print("============================")


def main() -> None:
    if len(sys.argv) < 2:
        print("Використання: python phonebook.py <назва_файлу.json>")
        sys.exit(1)

    filename: str = sys.argv[1]
    phonebook: PhoneBook = load_phonebook(filename)

    if "phones" not in phonebook:
        phonebook["phones"] = []

    while True:
        show_menu()
        choice: str = input("Виберіть дію (1-9): ")

        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            search_by_first_name(phonebook)
        elif choice == "3":
            search_by_last_name(phonebook)
        elif choice == "4":
            search_by_full_name(phonebook)
        elif choice == "5":
            search_by_phone(phonebook)
        elif choice == "6":
            search_by_city(phonebook)
        elif choice == "7":
            delete_by_phone(phonebook)
        elif choice == "8":
            update_by_phone(phonebook)
        elif choice == "9":
            save_phonebook(filename, phonebook)
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()