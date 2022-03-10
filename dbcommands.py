import sqlite3

conn = sqlite3.connect('./db/database.sqlite')

cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS items;
CREATE TABLE items(item_name TEXT NOT NULL, PRIMARY KEY(item_id)); 
WITHOUT ROWID""")

conn.commit()

conn.close()