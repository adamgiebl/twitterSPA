from bottle import response, get, post
import sqlite3
import json

##############################
@post("/items")
@post("/<language>/items")
def _():
  item = {
    "item_name": 'adam',
  }

  db = db_connect("./db/database.sqlite")

  try:  
    db.execute("""INSERT INTO items 
                VALUES(:item_name)""", item)
    db.commit()
    return item
  except Exception as ex:
    print(ex)
  finally:
    db.close()

##############################
@get("/items")
def _():

  db = db_connect("./db/database.sqlite")

  try:  
    items = json.dumps(db.execute("SELECT * FROM items").fetchall())
    print(items)

    return items
  except Exception as ex:
    print(ex)
  finally:
    db.close()


##############################
def create_json_from_sqlite_result(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

##############################
def db_connect(db_name):
  db = sqlite3.connect(db_name)
  db.row_factory = create_json_from_sqlite_result
  return db