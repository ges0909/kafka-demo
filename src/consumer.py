import datetime
import json

from confluent_kafka import Consumer

TOPICS: list[str] = ['topic1']
OVERALL_TIMEOUT: float = 10.0
POLL_TIMEOUT: float = 1.0

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    # 'security.protocol': 'SSL',
    # 'auto.offset.reset': 'earliest'
}


def kafka():
    messages = []

    consumer = Consumer(config)
    consumer.subscribe(TOPICS)

    end_time = datetime.datetime.now() + datetime.timedelta(seconds=OVERALL_TIMEOUT)

    while datetime.datetime.now() < end_time:
        msg = consumer.poll(timeout=POLL_TIMEOUT)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        messages.append(msg.value().decode("utf-8"))

    consumer.close()

    return {
        "messages": messages
    }


msgs = kafka()

print(json.dumps(msgs, indent=2))
