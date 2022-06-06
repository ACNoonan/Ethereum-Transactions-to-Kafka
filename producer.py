import json
import uuid
import time
import datetime
import string
import random
from random import randint
from kafka import KafkaProducer

# Declare folder path
folderName = "./kafkaKeys/"

# Declare producer
producer = KafkaProducer(
    bootstrap_servers="[HOSTNAME]:[PORT]",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
)

def generate_msg(tx_len = 64, act_len = 42):

    # Generate dict variables
    dt = datetime.datetime.now().isoformat()
    uuidentifier = str(uuid.uuid1())
    bn = randint(10000000,99999999)                                                                            # 8 digit random number
    ts = randint(1000000000,9999999999)                                                                        # 10 digit random number
    h = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=tx_len))   # 0x prefix + Random 64 digit alphanumeric 
    nonce = randint(1,999999)                                                                                  # 1-999999 random number
    bh = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=tx_len))  # 0x prefix + Random 64 digit alphanumeric
    ti = randint(1,999)                                                                                        # 1-999 random number
    fm = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
    to = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
    value = randint(1000000000000000000,99999999999999999999)                                                 # 20 digit random number (*)
    gas = randint(10000,99999999)                                                                              # 5 - 8 digit random number
    gp = randint(1000000000000,99999999999)                                                                                           # 12 digit random number (*)
    ie = randint(0,1)                                                                                          # binary/boolean
    txstatus = randint(0,1)                                                                                    # binary/boolean
    inp = '0x'                                                                                                 # 0x (*)
    ca = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
    cgu = (1000,999999999)                                                                                     # 4 - 10 digit random number (*)
    gu = randint(1000,99999)                                                                                   # 4 - 6 digit random number 
    c = randint(100000,9999999)                                                                                # 7 digit random number

    x = {
         "datetime":dt, 
         "uuid":uuidentifier,
         "blockNumber":bn,
         "timeStamp":ts,
         "hash":h,
         "nonce":nonce,
         "bh":bh,
         "transactionIndex":ti,
         "from":fm,
         "to":to,
         "value":value,
         "gas":gas,
         "gasPrice":gp,
         "isError":ie,
         "txreceipt_status":txstatus,
         "input":inp,
         "contractAddress":ca,
         "cumulativegasUsed":cgu,
         "gasUsed":gu,
         "confirmations":c
        }

    # Generate JSON from dict
    message = json.dumps(x)

    return message

for i in range(1,4):
    msg = generate_msg()
    producer.send('ethereum_transactions', msg.encode('utf-8'))
producer.flush()

