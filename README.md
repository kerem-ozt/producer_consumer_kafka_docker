# producer_consumer_kafka_docker
Docker imajı kullanarak kafka üzerinden producer-consumer uygulamalarının çalıştırılmsı.

Kafka'yı Docker ile çalıştırabilmek için çok popüler iki tane Docker image'ına ihtiyacımız var. 

- wurstmeister/zookeper
- wurstmeister/kafka

İlk olarak bu image'ları indirmek için bir docker-compose dosyası oluşturmamız gerekiyor. Repository içerisinde bulunan docker-compose.yml dosyası içerisinde bu iki image'ın indirilmesi için gerekli konfigürasyon bilgileri verilmiştir. 

Bu docker-compose dosyasının bulunduğu dizinde **docker-compose -f docker-compose.yml up -d** komutunu çalıştırarak dosya içerisinde belirtilen konteynırlarımızı oluşturmuş oluyoruz.

Konteynırlarımız çalışmaya başladıktan sonra **docker exec -it kafka /bin/sh** komutunu terinale girerek Kafka'nın shell'ine ulaşabiliriz.

Daha sonra sırasıyla **/opt, /kafka_versiyon, /bin** konumlarına gidip uygulamaları çalıştırmak üzere **kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic topic_name** komutu ile Kafka topic'imizi oluşturabiliriz.

Son olarak exit komutuyla Kafka shell'den çıkarak **python3 -m pip install kafka-python** ile repositoryde bulunan kodları çalıştırmak için gerekli kütüphaneyi indirebiliriz.

Artık ortamımız programlarımızın kullanımına hazır. İki farklı terminal açaraak birinde **conusmer.py** adlı dosyayı diğerindeyse **producer.py** isimli dosyayı çalıştırarak birinin ürettiği mesajları diğerine ilettiğini görebiliriz.
