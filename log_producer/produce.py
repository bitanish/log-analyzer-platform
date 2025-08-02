import json
import time
import uuid
from faker import Faker
from datetime import datetime
from kafka import KafkaProducer
import os

fake = Faker()

def generate_log(service_name):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": fake.random_element(elements=["INFO", "WARN", "ERROR"]),
        "service": service_name,
        "trace_id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "message": fake.sentence(nb_words=6),
        "meta": {
            "ip": fake.ipv4(),
            "location": fake.city()
        }
    }

def start_producing(rate, service):
    producer = KafkaProducer(
        bootstrap_servers='kafka:29092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    interval = 1.0 / rate  # seconds between logs

    print(f"[+] Starting producer for service '{service}' at {rate} logs/sec")

    while True:
        log = generate_log(service)
        producer.send('logs', value=log)
        time.sleep(interval)

if __name__ == "__main__":
    LOG_RATE = float(os.getenv("LOG_RATE", "1"))        # default 1 log/10 sec
    LOG_SERVICE = os.getenv("LOG_SERVICE", "default-service")

    start_producing(LOG_RATE,LOG_SERVICE)