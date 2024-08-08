import datetime

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
    consumer = Consumer(config)
    consumer.subscribe(TOPICS)

    end_time = datetime.datetime.now() + datetime.timedelta(seconds=OVERALL_TIMEOUT)

    while datetime.datetime.now() < end_time:
        msg = consumer.poll(timeout=POLL_TIMEOUT)
        print(msg)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        print(f'Message received: {msg.value().decode("utf-8")}')

    consumer.close()

    return


kafka()
