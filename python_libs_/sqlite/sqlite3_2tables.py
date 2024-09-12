import sqlite3


conn = sqlite3.connect('shop_database.db')


cur = conn.cursor()


create_table1 = '''
CREATE TABLE IF NOT EXISTS Table1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    email TEXT,
    price REAL NOT NULL,
    amount INTEGER NOT NULL,
    type TEXT
);
'''

create_table2 = '''
CREATE TABLE IF NOT EXISTS Table2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shop_location TEXT NOT NULL,
    customer_location TEXT NOT NULL,
    phone_number TEXT
);
'''


cur.execute(create_table1)
cur.execute(create_table2)


conn.commit()


conn.close()

print("Tables created successfully.")
