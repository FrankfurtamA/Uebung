import sqlite3

connection = sqlite3.connect('kursverwaltung.db')



connection.execute("INSERT INTO kursverwaltung (Name, Art, Schiene, Lehrkraft) VALUES ('10inf','GK', '1', 'RH');")


connection.commit()
connection.close()
