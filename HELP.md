# Apache Kafka & Python

- [Data Streaming mit Apache Kafka & Python](https://www.youtube.com/watch?v=BLIVlnObwAA)
- [Confluent's Python Client for Apache Kafka](https://github.com/confluentinc/confluent-kafka-python)
- [Choosing a Python Kafka client: A comparative analysis](https://quix.io/blog/choosing-python-kafka-client-comparative-analysis)

## Docker

```bash
docker compose up -d
```

## Python

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install confluent-kafka
```

## Test

```bash
python src/create_topic.py
python src/producer.py
python src/consumer.py
```
