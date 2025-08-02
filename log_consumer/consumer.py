import asyncio
import json
import os
from aiokafka import AIOKafkaConsumer
from db import insert_logs_es
from metrics import log_ingested_counter, insert_failure_counter, start_metrics_server

KAFKA_BROKER = os.getenv("KAFKA_BROKER_URL", "kafka:29092")
TOPIC = "logs"
BATCH_SIZE = 100

async def consume():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        enable_auto_commit=False
    )

    await consumer.start()
    print("Consumer started")

    batch = []
    try:
        async for msg in consumer:
            batch.append(msg.value)

            if len(batch) >= BATCH_SIZE:
                await flush_batch(consumer, batch)
                batch = []

            # Timeout flush
            await asyncio.sleep(0.001)  # let event loop cycle

    finally:
        if batch:
            await flush_batch(consumer, batch)
        await consumer.stop()


async def flush_batch(consumer, batch):
    try:
        await insert_logs_es(batch)
        log_ingested_counter.inc(len(batch))
        await consumer.commit()
    except Exception as e:
        insert_failure_counter.inc()
        print(f"[ERROR] Batch insert failed: {e}")

if __name__ == "__main__":
    start_metrics_server()
    asyncio.run(consume())
