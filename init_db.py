import sqlite3

connection = sqlite3.connect('users.db')


with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

cur.execute("INSERT INTO users (username, password,fname,lname,email) VALUES (?, ?,?,?,?)",
            ('Apurva','Ranaa','Apurva','Bhavanasi','apurva@gmail.com')
            )
cur = connection.cursor()
connection.commit()
connection.close()
