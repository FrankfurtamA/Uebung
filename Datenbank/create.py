import sqlite3

connection = sqlite3.connect('kursverwaltung.db')

sql_create = "Create table Vokabeltest (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Art TEXT NOT NULL, Schiene TEXT NOT NULL, Lehrkraft TEXT NOT NULL, Anmerkung TEXT))"

connection.execute(sql_create)

connection.commit()
connection.close()