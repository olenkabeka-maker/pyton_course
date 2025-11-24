SELECT first_name AS "Ім'я", last_name AS "Прізвище"
FROM employees;

SELECT DISTINCT department_id
FROM employees;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name AS "Ім'я",
       last_name AS "Прізвище",
       salary,
       salary * 0.12 AS pension_fund
FROM employees;

SELECT MAX(salary) AS max_salary,
       MIN(salary) AS min_salary
FROM employees;

SELECT first_name AS "Ім'я",
       last_name AS "Прізвище",
       ROUND(salary / 12.0, 2) AS monthly_salary
FROM employees;