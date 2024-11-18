import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="project_db",
    user="postgres",
    password="123456"
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS departments")

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO departments (department_name) VALUES ('Administration')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('IT')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('Design')")

connection.commit()

cursor.execute("SELECT * FROM departments")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
