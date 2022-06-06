import json
import uuid
import time
import datetime
import string
import random
from random import randint

class EthereumTransaction():
    def generate_ethereum_transaction_message (self, tx_len = 64, act_len = 42, i = 0):

        # Generate dict variables
        dt = datetime.datetime.now().isoformat()
        uuid = str(uuid.uuid1())
        bn = randint(10000000,99999999)                                                                            # 8 digit random number
        ts = randint(1000000000,9999999999)                                                                        # 10 digit random number
        h = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=tx_len))   # 0x prefix + Random 64 digit alphanumeric 
        nonce = randint(1,999999)                                                                                  # 1-999999 random number
        bh = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=tx_len))  # 0x prefix + Random 64 digit alphanumeric
        ti = randint(1,999)                                                                                        # 1-999 random number
        fm = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
        to = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
        value = randint(11111111111111111111,99999999999999999999)                                                 # 20 digit random number (*)
        gas = randint(11111,99999999)                                                                              # 5 - 8 digit random number
        gp = "gasPrice"                                                                                            # 12 digit random number (*)
        ie = randint(0,1)                                                                                          # binary/boolean
        txstatus = randint(0,1)                                                                                    # binary/boolean
        inp = '0x'                                                                                                 # 0x (*)
        ca = '0x' + ''.join(random.choices(string.ascii_lowercase+string.digits+string.ascii_uppercase,k=act_len)) # 0x prefix + Random 42 digit alphanumeric
        cgu = (1111,999999999)                                                                                     # 4 - 10 digit random number (*)
        gu = randint(1111,99999)                                                                                   # 4 - 6 digit random number 
        c = randint(111111,9999999)                                                                                # 7 digit random number

        # Declare dict
        x = {
             "datetime":dt, 
             "uuid":uuid,
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


        # Convert dict to JSON 
        message = json.dumps(x)

        # Pass argument to Key
        key = i

        return message, key