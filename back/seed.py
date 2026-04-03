#portfolio
#handle: _MUMINUL__ISLAM___

#CODE

import sqlite3
conn=sqlite3.connect("app.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products(
               product_id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_name TEXT,
               product_model TEXT,
               product_core INTEGER)
""")
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","i3-12100",4))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","i5-12400",6))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","i7-12700",8))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","i5-14400",10))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","i5-14600",14))

cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","7400",6))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","7600X",6))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","8300G",4))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","9900X",12))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","8700G",8))

cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","Ultra5",14))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","Ultra7",20))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("Intel","Ultra9",24))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","9950X3D",16))
cursor.execute("INSERT INTO products (product_name, product_model, product_core) VALUES (?,?,?)", ("AMD","9600X",6))

               
conn.commit()

cursor.execute("SELECT * FROM products")
rows=cursor.fetchall()
for row in rows:
    print(row)