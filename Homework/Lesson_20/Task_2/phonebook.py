import json
import sys
import os

def load_phonebook(filename):     # Завантаження телефонної книги з файлу
    if not os.path.exists(filename):
        print(f"Помилка: файл {filename} не знайдено!")
        sys.exit(1)

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_phonebook(filename, data):   # Збереження телефонної книги у файл
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Дані збережено!")


def add_entry(phonebook):             # Додавання нового запису
    print("\n=== Додавання нового запису ===")
    name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    phone = input("Введіть телефон: ")
    city = input("Введіть місто: ")

    new_entry = {
        "name": name,
        "lastName": last_name,
        "phone": phone,
        "city": city
    }

    phonebook['phones'].append(new_entry)
    print("Запис додано!")


def search_by_first_name(phonebook):   # Пошук за ім'ям
    name = input("Введіть ім'я для пошуку: ")
    results = [p for p in phonebook['phones'] if p['name'].lower() == name.lower()]

    if results:
        print(f"\nЗнайдено {len(results)} запис(ів):")
        for r in results:
            print(f"  {r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")
    else:
        print("Нічого не знайдено.")


def search_by_last_name(phonebook):    # Пошук за прізвищем
    last_name = input("Введіть прізвище для пошуку: ")
    results = [p for p in phonebook['phones'] if p['lastName'].lower() == last_name.lower()]

    if results:
        print(f"\nЗнайдено {len(results)} запис(ів):")
        for r in results:
            print(f"  {r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")
    else:
        print("Нічого не знайдено.")


def search_by_full_name(phonebook):    # Пошук за повним ім'ям
    name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")

    results = [p for p in phonebook['phones']
               if p['name'].lower() == name.lower() and p['lastName'].lower() == last_name.lower()]

    if results:
        print(f"\nЗнайдено {len(results)} запис(ів):")
        for r in results:
            print(f"  {r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")
    else:
        print("Нічого не знайдено.")


def search_by_phone(phonebook):        # Пошук за телефоном
    phone = input("Введіть телефон для пошуку: ")
    results = [p for p in phonebook['phones'] if p['phone'] == phone]

    if results:
        for r in results:
            print(f"{r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")
    else:
        print("Нічого не знайдено.")


def search_by_city(phonebook):         # Пошук за містом
    city = input("Введіть місто для пошуку: ")
    results = [p for p in phonebook['phones'] if p['city'].lower() == city.lower()]

    if results:
        for r in results:
            print(f"{r['name']} {r['lastName']}, тел: {r['phone']}, місто: {r['city']}")
    else:
        print("Нічого не знайдено.")


def delete_by_phone(phonebook):        # Видалення запису
    phone = input("Введіть телефон для видалення: ")
    results = [p for p in phonebook['phones'] if p['phone'] == phone]

    if not results:
        print("Запис не знайдено.")
        return

    confirm = input("Видалити цей запис? (y/n): ")
    if confirm.lower() == 'y':
        phonebook['phones'] = [p for p in phonebook['phones'] if p['phone'] != phone]
        print("Запис видалено.")
    else:
        print("Видалення скасовано.")


def update_by_phone(phonebook):        # Оновлення запису
    phone = input("Введіть телефон для оновлення: ")

    for p in phonebook['phones']:
        if p['phone'] == phone:
            print(f"Знайдено: {p['name']} {p['lastName']} ({p['city']})")
            new_name = input(f"Нове ім'я [{p['name']}]: ") or p['name']
            new_last = input(f"Нове прізвище [{p['lastName']}]: ") or p['lastName']
            new_phone = input(f"Новий телефон [{p['phone']}]: ") or p['phone']
            new_city = input(f"Нове місто [{p['city']}]: ") or p['city']

            p.update({"name": new_name, "lastName": new_last, "phone": new_phone, "city": new_city})
            print("♻️ Запис оновлено.")
            return

    print("Запис не знайдено.")


def show_menu():
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


def main():
    if len(sys.argv) < 2:
        print("Використання: python phonebook.py <назва_файлу.json>")
        sys.exit(1)

    filename = sys.argv[1]

    phonebook = load_phonebook(filename)
    if 'phones' not in phonebook:
        phonebook['phones'] = []

    while True:
        show_menu()
        choice = input("Виберіть дію (1-9): ")

        if choice == '1':
            add_entry(phonebook)
        elif choice == '2':
            search_by_first_name(phonebook)
        elif choice == '3':
            search_by_last_name(phonebook)
        elif choice == '4':
            search_by_full_name(phonebook)
        elif choice == '5':
            search_by_phone(phonebook)
        elif choice == '6':
            search_by_city(phonebook)
        elif choice == '7':
            delete_by_phone(phonebook)
        elif choice == '8':
            update_by_phone(phonebook)
        elif choice == '9':
            save_phonebook(filename, phonebook)
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()