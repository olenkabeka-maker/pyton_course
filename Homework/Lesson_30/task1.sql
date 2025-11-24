"""Створіть таблицю на ваш вибір у зразку бази даних SQLite, перейменуйте її та додайте новий стовпець. 
Вставте кілька рядків у таблицю. Також виконайте оператори UPDATE та DELETE для вставлених рядків"""

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS staff;

/*створюю таблицю employees на 4 колонки*/
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
);

/*додаю дані в колонки*/
INSERT INTO employees (name, position, salary) VALUES ('Alona Lashchenko', 'specialist', 17000);
INSERT INTO employees (name, position, salary) VALUES ('Yana Sharapova', 'specialist', 16565);
INSERT INTO employees (name, position, salary) VALUES ('Yana Babich', 'manager', 19638);

/*переіменовую таблицю на staff*/
ALTER TABLE employees RENAME TO staff;

/*додаю нову колонку*/
ALTER TABLE staff ADD COLUMN date_hired DATE;

/*оновлюю дані в таблиці*/
UPDATE staff
SET date_hired = '2017-08-01'
WHERE name = 'Alona Lashchenko';

SELECT * FROM staff;

/*видаляю з таблиціі*/
DELETE FROM staff
WHERE name = 'Yana Babich';

/*додаю нового працівника*/
INSERT INTO staff (name, position, salary, date_hired) VALUES ('Maryna Dmytrivna', 'deputy chief', 25700, '2019-09-01');

/*оновлюю дані в таблиці*/
UPDATE staff
SET date_hired = '2015-07-23'
WHERE name = 'Yana Sharapova';

SELECT * FROM staff;