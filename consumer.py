import json 
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        #booystrap_servers='172.18.0.1',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))
