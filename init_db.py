import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    restaurant_name TEXT,
    item_name TEXT,
    amount REAL,
    status TEXT,
    created_at TEXT,
    processed_at TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized: orders.db")
