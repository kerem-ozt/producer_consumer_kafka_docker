import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer

# Mesajın JSON formatında döndürülmesi 
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    #bootsrap_servers=['172.18.0.1'],
    value_serializer=serializer
)


if __name__ == '__main__':
    # Mesaj üretilmesi için kurulmuş döngü
    while True:
        # mesaj üretilmesi
        dummy_message = generate_message()
        
        # Mesaj topiğinin gönderilmesi
        print(f'Created message @ {datetime.now()} | message = {str(dummy_message)}')
        producer.send('message', dummy_message)
        
        # Bekleme süresi atanması
        time.sleep(8)
