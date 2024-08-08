from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['topic1'])

while True:
    msg = consumer.poll(timeout=1.0)

    print(msg)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    print(f'Message received: {msg.value().decode("utf-8")}')

consumer.close()
