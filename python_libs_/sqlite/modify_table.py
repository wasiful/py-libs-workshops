import sqlite3


conn = sqlite3.connect('shop_database.db')
cur = conn.cursor()


cur.execute("UPDATE Table2 SET shop_location = 'New City' WHERE shop_location = 'New York'")


cur.execute("UPDATE Table2 SET phone_number = '0' WHERE phone_number IS NULL OR phone_number = ''")
cur.execute("UPDATE Table1 SET email = '0' WHERE email IS NULL OR email = ''")


cur.execute("INSERT INTO Table1 (name, family_name, date, email, price, amount, type) VALUES ('Emily White', 'White', '2024-09-13', 'emily@example.com', 120.00, 3, 'Home Appliance')")
cur.execute("INSERT INTO Table2 (shop_location, customer_location, phone_number) VALUES ('San Francisco', 'Houston', '555-9999')")


cur.execute("DELETE FROM Table1 WHERE id = 5")
cur.execute("DELETE FROM Table2 WHERE id = 5")


cur.execute("ALTER TABLE Table1 ADD COLUMN family_name TEXT")
cur.execute("UPDATE Table1 SET family_name = 'Doe' WHERE id = 1")
cur.execute("UPDATE Table1 SET family_name = 'Smith' WHERE id = 2")
cur.execute("UPDATE Table1 SET family_name = 'Johnson' WHERE id = 3")
cur.execute("UPDATE Table1 SET family_name = 'Brown' WHERE id = 4")
cur.execute("UPDATE Table1 SET family_name = 'White' WHERE id = 6")


cur.execute("SELECT SUM(amount) FROM Table1")
total_amount_sold = cur.fetchone()[0]
print(f"Total amount sold: {total_amount_sold}")


cur.execute('''
    CREATE TABLE IF NOT EXISTS SameCityOrAddress (
        id INTEGER PRIMARY KEY,
        name TEXT,
        family_name TEXT,
        email TEXT,
        shop_location TEXT,
        customer_location TEXT,
        phone_number TEXT
    )
''')
cur.execute('''
    INSERT INTO SameCityOrAddress (id, name, family_name, email, shop_location, customer_location, phone_number)
    SELECT t1.id, t1.name, t1.family_name, t1.email, t2.shop_location, t2.customer_location, t2.phone_number
    FROM Table1 t1
    JOIN Table2 t2 ON t1.id = t2.id
    WHERE t2.customer_location IN (
        SELECT customer_location FROM Table2
        GROUP BY customer_location
        HAVING COUNT(customer_location) > 1
    )
''')


conn.commit()
conn.close()

print("All operations completed.")
