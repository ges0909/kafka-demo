# Apache Kafka & Python

- [Data Streaming mit Apache Kafka & Python](https://www.youtube.com/watch?v=BLIVlnObwAA)
- [Confluent's Python Client for Apache Kafka](https://github.com/confluentinc/confluent-kafka-python)
- [Choosing a Python Kafka client: A comparative analysis](https://quix.io/blog/choosing-python-kafka-client-comparative-analysis)

## Security

```bash
winget install -e --id ShiningLight.OpenSSL
```

```bash
# Create the certification authority key and certificate 
openssl req -new -nodes -x509 -days 365 -newkey rsa:2048 -keyout ./certs/ca.key -out ./certs/ca.rt -config "C:\Program Files\OpenSSL-Win64\bin\cnf\openssl.cnf"

# Convert authority key and certificate files to a .pem file
cat ./certs/ca.rt ./certs/ca.key > ./certs/ca.pem

# Create the server key and certificate
openssl req -new -newkey rsa:2048 -keyout ./certs/kafka.key -out ./certs/kafka.csr -config "C:\Program Files\OpenSSL-Win64\bin\cnf\openssl.cnf"

# Sign the certificate with the certificate authority
openssl x509 -req -days 365 -in ./certs/kafka.csr -CA ./certs/ca.rt -CAkey ./certs/ca.key -CAcreateserial -out ./certs/kafka.crt -extfile "C:\Program Files\OpenSSL-Win64\bin\cnf\
openssl.cnf" -extensions v3_req

# Convert server certificate to the pkcs12 format
openssl pkcs12 -export -in ./certs/kafka.crt -inkey ./certs/kafka.key -chain -CAfile ./certs/ca.pem -name kafka -out ./certs/kafka.p12 -password pass:123456

# Create broker keystore and import the certificate
 keytool -importkeystore -deststorepass 123456 -destkeystore ./certs/kafka.pkcs12 -srckeystore ./certs/kafka.p12 -deststoretype PKCS12 -srcstoretype PKCS12 -noprompt -srcstorepass
 123456
```

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
