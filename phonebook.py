import json
import sys
import os

def load_phonebook(filename):
    """Завантаження телефонної книги з JSON ololo tratata"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print(f"Файл {filename} не знайдено. Буде створено новий.")
        return {}

def save_phonebook(filename, data):
    """Збереження телефонної книги у JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_record(phonebook):
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    phone = input("Введіть номер телефону: ")
    city = input("Введіть місто або штат: ")

    if phone in phonebook:
        print("Такий номер уже існує!")
    else:
        phonebook[phone] = {"ім'я": name, "прізвище": surname, "місто": city}
        print("✅ Запис додано!")

def search_by_name(phonebook):
    name = input("Введіть ім'я: ")
    for phone, info in phonebook.items():
        if info["ім'я"].lower() == name.lower():
            print(phone, info)

def search_by_surname(phonebook):
    surname = input("Введіть прізвище: ")
    for phone, info in phonebook.items():
        if info["прізвище"].lower() == surname.lower():
            print(phone, info)

def search_by_fullname(phonebook):
    fullname = input("Введіть повне ім'я (Ім'я Прізвище): ")
    for phone, info in phonebook.items():
        if f"{info["ім'я"]} {info['прізвище']}".lower() == fullname.lower():
            print(phone, info)

def search_by_phone(phonebook):
    phone = input("Введіть номер телефону: ")
    if phone in phonebook:
        print(phone, phonebook[phone])
    else:
        print("Не знайдено.")

def search_by_city(phonebook):
    city = input("Введіть місто або штат: ")
    for phone, info in phonebook.items():
        if info["місто"].lower() == city.lower():
            print(phone, info)

def delete_record(phonebook):
    phone = input("Введіть номер телефону для видалення: ")
    if phone in phonebook:
        del phonebook[phone]
        print("Запис видалено.")
    else:
        print("Такого номера немає.")

def update_record(phonebook):
    phone = input("Введіть номер телефону для оновлення: ")
    if phone in phonebook:
        print("Поточні дані:", phonebook[phone])
        name = input("Нове ім'я (або Enter, щоб залишити): ")
        surname = input("Нове прізвище (або Enter, щоб залишити): ")
        city = input("Нове місто (або Enter, щоб залишити): ")

        if name:
            phonebook[phone]["ім'я"] = name
        if surname:
            phonebook[phone]["прізвище"] = surname
        if city:
            phonebook[phone]["місто"] = city

        print("Запис оновлено.")
    else:
        print("Такого номера немає.")

def main():
    if len(sys.argv) < 2:
        print("Використання: python phonebook.py <назва_файлу>.json")
        sys.exit(1)

    filename = sys.argv[1]
    phonebook = load_phonebook(filename)

    while True:
        print("""
Телефонна книга
1. Додати новий запис
2. Пошук за іменем
3. Пошук за прізвищем
4. Пошук за повним ім'ям
5. Пошук за номером телефону
6. Пошук за містом/штатом
7. Видалити запис
8. Оновити запис
9. Вихід
        """)

        choice = input("Оберіть дію (1-9): ")

        if choice == "1":
            add_record(phonebook)
        elif choice == "2":
            search_by_name(phonebook)
        elif choice == "3":
            search_by_surname(phonebook)
        elif choice == "4":
            search_by_fullname(phonebook)
        elif choice == "5":
            search_by_phone(phonebook)
        elif choice == "6":
            search_by_city(phonebook)
        elif choice == "7":
            delete_record(phonebook)
        elif choice == "8":
            update_record(phonebook)
        elif choice == "9":
            save_phonebook(filename, phonebook)
            print("Дані збережено. Вихід із програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()