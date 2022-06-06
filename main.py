import sys
import argparse
import time
import random
from kafka import KafkaProducer
from eth_tx_producer import EthereumTransaction


def produce_msgs(security_protocol='SSL',
                 folderName = './kafkaKeys/',
                 hostname = 'kafka-sa-homework-adamnoonan-3697.aivencloud.com',
                 port = '17827',
                 topic_name = 'eth_transactions',
                 nr_messages = -1,
                 max_waiting_time_in_sec = 5):
    if security_protocol.upper() == 'SSL':
        producer = KafkaProducer(
            bootstrap_servers=hostname + ':' + port,
            security_protocol='SSL',
            ssl_cafile=folderName+'ca.pem',
            ssl_certfile=folderName+'service.cert',
            ssl_keyfile=folderName+'service.key',
        )
    else:
        sys.exit('SSL is the only security protocol currently supported.')

    if nr_messages < 0:
        nr_messages = float('inf')
    i = 0


    # Sleeping time
    sleep_time = random.randint(0, int(max_waiting_time_in_sec * 10000))/10000
    print('Sleeping for...'+str(sleep_time)+'s')
    time.sleep(sleep_time)

    # Force flushing of all messages
    if ( i % 100) == 0:
        producer.flush()
    i = i + 1


def main():
    produce_msgs()


if __name__ == '__main__':
    main()