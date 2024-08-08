from confluent_kafka import Producer

# Essential security settings to enable client authentication and SSL encryption
config = {
    'bootstrap.servers': 'localhost:9092',

    # # config.setProperty("security.protocol", "SSL");
    # 'security.protocol': 'SSL',
    #
    # # config.setProperty("ssl.truststore.location", "..\\Kafka_Certs\\personal.jks");
    # # config.setProperty("ssl.truststore.type", "JKS");
    # # config.setProperty("ssl.truststore.password", "123456");
    # 'ssl.truststore.location': '/etc/security/tls/kafka.client.truststore.jks',
    # 'ssl.truststore.password': 'test1234',
    #
    # # config.setProperty("ssl.keystore.location", "..\\Kafka_Certs\\personal.jks");
    # # config.setProperty("ssl.keystore.type", "JKS");
    # # config.setProperty("ssl.keystore.password", "123456");
    # 'ssl.keystore.location': '/etc/security/tls/kafka.client.keystore.jks',
    # 'ssl.keystore.password': 'test1234',
    #
    # # config.setProperty("ssl.key.password", "123456");
    # 'ssl.key.password': 'test1234'
}

producer = Producer(config)

messages = ["meine message", "hallo", "hallo coders", "tim"]


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} in partition {msg.partition()}')


for msg in messages:
    # Trigger any available delivery report callbacks from previous produce() calls
    producer.poll(0)

    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    producer.produce('topic1', msg.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
producer.flush()
