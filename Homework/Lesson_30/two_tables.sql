DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS contacts;

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city INTEGER,
    phone_number TEXT,
    FOREIGN KEY (city) REFERENCES cities(id)
);

INSERT INTO cities (name) VALUES ('Kyiv');
INSERT INTO cities (name) VALUES ('Lviv');
INSERT INTO cities (name) VALUES ('Berdiansk');

INSERT INTO contacts (name, city, phone_number) VALUES ('Alona Lashchenko', 1, '+380501234567');
INSERT INTO contacts (name, city, phone_number) VALUES ('Yana Sharapova', 2, '+380671112233');
INSERT INTO contacts (name, city, phone_number) VALUES ('Yana Babich', 3, '+380931234567');

/*Запит на отримання всіх контактів з назвами міст*/

SELECT c.name AS contact_name, ci.name AS city_name, c.phone_number
FROM contacts c
LEFT JOIN cities ci ON c.city = ci.id;

/*запит на всі контакти у Києві*/

SELECT name, phone_number
FROM contacts
WHERE city = (SELECT id FROM cities WHERE name = 'Kyiv');
