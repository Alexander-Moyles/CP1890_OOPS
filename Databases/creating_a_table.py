import sqlite3

#conn = sqlite3.connect('class_example.sqlite')

#c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks INTEGER);"""
print(query)
#c.execute(query)
print("Table has been created")

query = """INSERT into students VALUES ({}, {}, {}, {})""".format(1, 'Arun Rameshbabu', 30, 100)
print(query)
#c.execute("""INSERT into students VALUES ({}, {}, {}, {})""".format(1, 'Arun Rameshbabu', 30, 100))
conn.commit()
conn.close()

