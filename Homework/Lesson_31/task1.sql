"""Використайте зразок бази даних SQLite hr.db та напишіть SQL-запити"""

/* 1. Ім’я, прізвище, номер відділу та назва відділу */

SELECT e.first_name,
       e.last_name,
       e.department_id,
       d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;


/* 2. Ім’я, прізвище, відділ, місто та штат/область */

SELECT e.first_name,
       e.last_name,
       d.department_name,
       l.city,
       l.state_province
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN locations l ON d.location_id = l.location_id;


/* 3. Співробітники відділів 80 або 40 */

SELECT e.first_name,
       e.last_name,
       e.department_id,
       d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);

/* 4. Усі відділи, включно з тими, де немає співробітників */

SELECT d.department_name,
       d.department_id,
       e.first_name,
       e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;


/* 5. Імена співробітників + ім'я їхнього керівника */

SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;


/* 6. Посада, ім’я, прізвище та різниця між макс. зарплатою за посадою і фактичною зарплатою */

SELECT j.job_title,
       e.first_name || ' ' || e.last_name AS employee_name,
       (j.max_salary - e.salary) AS salary_difference
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;


/* 7. Посада та середня зарплата співробітників */

SELECT j.job_title,
       AVG(e.salary) AS average_salary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;


/* 8. Повне ім’я і зарплата співробітників, які працюють у відділах, що розташовані в Лондоні */

SELECT e.first_name || ' ' || e.last_name AS full_name,
       e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';


/* 9. Назва відділу та кількість співробітників у кожному */

SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;