import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('shop_database.db')

# Create a cursor object
cur = conn.cursor()

# Retrieve and display data from Table1
cur.execute("SELECT * FROM Table1")
table1_data = cur.fetchall()
print("Table 1 Data:")
for row in table1_data:
    print(row)

# Retrieve and display data from Table2
cur.execute("SELECT * FROM Table2")
table2_data = cur.fetchall()
print("\nTable 2 Data:")
for row in table2_data:
    print(row)

# Close the connection
conn.close()
