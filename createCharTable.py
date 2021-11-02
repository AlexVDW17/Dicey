import sqlite3

conn = sqlite3.connect('characters.db')
c = conn.cursor()
c.execute('CREATE TABLE characters (name VARCHAR, level VARCHAR, class VARCHAR)')
conn.commit()