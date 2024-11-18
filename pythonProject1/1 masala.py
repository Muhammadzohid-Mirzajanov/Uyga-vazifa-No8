import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="project_db",
    user="postgres",
    password="123456"
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    position TEXT,
    salary DECIMAL(10, 2),
    hire_date DATE,
    department_id INT
)
""")

employees_data = [
    (1, "Ali", "Karimov", "Manager", 3000.00, "2020-03-15", 1),
    (2, "Nodira", "Toirova", "Developer", 2500.50, "2021-05-10", 2),
    (3, "Shoxruh", "Abdullayev", "Designer", 2200.75, "2022-01-22", 3),
    (4, "Zarina", "Abdullayeva", "HR Specialist", 1800.25, "2019-11-11", 1),
    (5, "Jasur", "Aliyev", "Developer", 2400.80, "2023-02-01", 2),
]

cursor.executemany("""
INSERT INTO employees (id, first_name, last_name, position, salary, hire_date, department_id)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""", employees_data)

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Position':<15} {'Salary':<10} {'Hire Date':<12} {'Dept ID':<8}")
print("-" * 85)
for row in rows:
    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15} {row[4]:<10.2f} {row[5]:<12} {row[6]:<8}")

connection.commit()
connection.close()
