SELECT first_name || ' ' || last_name AS "Full Name"
FROM employees;

SELECT * FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
WHERE salary > 2500;

SELECT * FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT * FROM employees
WHERE salary IN (2400, 3000);

SELECT * FROM employees
WHERE salary BETWEEN 2000 AND 3000;

SELECT * FROM employees
WHERE first_name LIKE '%a%';

SELECT * FROM projects
WHERE end_date IS NULL;

SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;
