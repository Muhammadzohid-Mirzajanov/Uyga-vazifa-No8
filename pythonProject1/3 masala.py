import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="project_db",
    user="postgres",
    password="123456"
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS project")

cursor.execute("""
CREATE TABLE IF NOT EXISTS project (
    id SERIAL PRIMARY KEY,
    project_name TEXT,
    start_date DATE,
    end_date DATE,
    budget INT
)
""")

cursor.execute("INSERT INTO project (id, project_name, start_date, end_date, budget) VALUES (1, 'New Website', '2023-01-10', '2023-06-30', 50000)")
cursor.execute("INSERT INTO project (id, project_name, start_date, end_date, budget) VALUES (2, 'Mobile App', '2022-08-15', '2023-03-20', 30000)")
cursor.execute("INSERT INTO project (id, project_name, start_date, end_date, budget) VALUES (3, 'CRM System', '2024-02-01', NULL, 60000)")

connection.commit()

cursor.execute("SELECT * FROM project")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
