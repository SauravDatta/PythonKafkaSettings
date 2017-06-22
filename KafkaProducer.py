from confluent_kafka import Producer


class KafkaProducer:
    producertopic = "test.topic"

    def __init__(self):
        # Replace broker list with your brokers 
        self.producer = Producer({"bootstrap.servers": 'mybroker,mybroker2'})

    def send(self, producertopic, inputdata):
        self.producer.produce(producertopic, inputdata)
