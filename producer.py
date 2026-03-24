from kafka import KafkaProducer
import json
import time
import uuid
from datetime import datetime
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

restaurants = ["Pizza Hut", "Chipotle", "McDonalds", "Dominos", "Subway"]
items = ["Pizza", "Burrito", "Burger", "Pasta", "Sandwich"]
customers = ["Alice", "Bob", "Charlie", "David", "Emma"]

topic_name = "order_events"

print("Sending order events to Kafka...")

while True:
    order = {
        "order_id": str(uuid.uuid4())[:8],
        "customer_name": random.choice(customers),
        "restaurant_name": random.choice(restaurants),
        "item_name": random.choice(items),
        "amount": round(random.uniform(10, 50), 2),
        "status": "placed",
        "created_at": datetime.utcnow().isoformat()
    }

    producer.send(topic_name, value=order)
    producer.flush()

    print(f"Sent: {order}")
    time.sleep(3)
