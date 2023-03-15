import sqlite3

connection = sqlite3.connect('kursverwaltung.db')


cursor = connection.cursor()
select = "SELECT * FROM kursverwaltung"

verwaltung =  cursor.execute(select).fetchall()

connection.execute(select)

print(verwaltung)


connection.close()





