from kafka import KafkaConsumer
import json
import sqlite3
from datetime import datetime

consumer = KafkaConsumer(
    "order_events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="order-tracking-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

conn = sqlite3.connect("orders.db", check_same_thread=False)
cursor = conn.cursor()

print("Listening for Kafka messages...")

for message in consumer:
    order = message.value
    processed_at = datetime.utcnow().isoformat()

    cursor.execute("""
        INSERT OR REPLACE INTO orders (
            order_id, customer_name, restaurant_name, item_name,
            amount, status, created_at, processed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order["order_id"],
        order["customer_name"],
        order["restaurant_name"],
        order["item_name"],
        order["amount"],
        order["status"],
        order["created_at"],
        processed_at
    ))

    conn.commit()
    print(f"Processed and stored: {order['order_id']}")
