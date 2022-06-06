#import string
#import random
#from random import randint
#
#length=42
#randomstr = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=length))
#address = '0x' + randomstr
#
##print(randomstr)
#
#
#
#f = randint(0,1)
#print(f)

from kafka import KafkaProducer

#folderName = "C:/Users/Adam/Documents/Development/Aiven/aiven-kafka-producer/kafkaKeys/"
folderName = "./kafkaKeys/"

producer = KafkaProducer(
    bootstrap_servers="kafka-sa-homework-adamnoonan-3697.aivencloud.com:17827",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
)


for i in range(1,4):
    message = "message number {}".format(i)
    print("sending: {}".format(message))
    producer.send("test-topic",message.encode("utf-8"))

producer.flush()