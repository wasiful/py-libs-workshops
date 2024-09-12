import sqlite3


conn = sqlite3.connect('shop_database.db')


cur = conn.cursor()


cur.execute('''
INSERT INTO Table1 (name, date, email, price, amount, type) VALUES
('John Doe', '2024-09-12', 'john@example.com', 150.75, 2, 'Electronics'),
('Jane Smith', '2024-09-11', 'jane@example.com', 299.99, 1, 'Laptop'),
('Alice Johnson', '2024-09-10', 'alice@example.com', 49.99, 5, 'Books'),
('Bob Brown', '2024-09-09', 'bob@example.com', 99.99, 3, 'Clothing'),
('Charlie Green', '2024-09-08', 'charlie@example.com', 199.99, 1, 'Smartphone')
''')


cur.execute('''
INSERT INTO Table2 (shop_location, customer_location, phone_number) VALUES
('New York', 'Los Angeles', '555-1234'),
('San Francisco', 'Houston', '555-5678'),
('Chicago', 'Chicago', '555-8765'),
('Seattle', 'Dallas', '555-4321'),
('Miami', 'Miami', '555-9876')
''')


conn.commit()


conn.close()

print("Data inserted successfully.")
