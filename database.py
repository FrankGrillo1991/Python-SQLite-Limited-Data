import sqlite3

#connecting to sqlite database
connection_obj = sqlite3.connect("geek.db")

#cursor object
cursor_obj = connection_obj.cursor()


# Create table GEEK if it does not exist
create_table_sql = '''
CREATE TABLE IF NOT EXISTS GEEK (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    skill TEXT
);
'''
cursor_obj.execute(create_table_sql)

# Optionally, insert sample data if table is empty
cursor_obj.execute('SELECT COUNT(*) FROM GEEK')
if cursor_obj.fetchone()[0] == 0:
    sample_data = [
        ("Alice", 25, "Python"),
        ("Bob", 30, "Java"),
        ("Charlie", 22, "C++"),
        ("Diana", 28, "JavaScript"),
        ("Eve", 35, "Go"),
        ("Frank", 27, "Ruby")
    ]
    cursor_obj.executemany('INSERT INTO GEEK (name, age, skill) VALUES (?, ?, ?)', sample_data)

#to select all column we will use
statement = """SELECT * FROM GEEK"""
cursor_obj.execute(statement)


# Print column names
column_names = [description[0] for description in cursor_obj.description]
print("Column names:", column_names)

print("Limited data:")
output = cursor_obj.fetchmany(5)
for row in output:
    print(row)

connection_obj.commit()

#close the connection
connection_obj.close()












