import sqlite3 as s

connection = s.connect("data.db")
cursor = connection.cursor()

new_rows =[('Cats','Cat City','2088.10.17'),('Dogs','Dogs City','2017.02.23')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
connection.commit()

cursor.execute("SELECT * FROM events WHERE band ='Cats'")

result = cursor.fetchall()

print(result)