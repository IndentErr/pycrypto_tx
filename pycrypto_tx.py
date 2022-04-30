import cryptocompare
import datetime
import logging
from web3 import Web3

class trading:
    def __init__(self,crypto_num,url,start_address,start_privatekey,destination_address):
        self.crypto_num = crypto_num
        self.url = url
        self.start_address = start_address
        self.start_privatekey = start_privatekey
        self.destination_address = destination_address
    
    def transaction_eth(self):
        web3 = Web3(Web3.HTTPProvider(self.url))
        nonce = web3.eth.getTransactionCount(self.start_address)
        transaction_info = {"nonce":nonce, "to":self.destination_address, "value": web3.toWei(self.crypto_num,"ether"), "gas": 2000000, 'gasPrice': web3.toWei('50', 'gwei')}
        transaction_sign = web3.eth.account.sign_transaction(transaction_info,self.start_privatekey)

    def transaction_btc(self):
        transaction_info = {}

class price:

    def __init__(self,cash,crypto_num,crypto_type,cash_type):

        self.cash = cash
        self.crypto_num = crypto_num
        self.crypto_type = crypto_type
        self.cash_type = cash_type
        self.price = 0
    def price_calculator(self):
        
        price_raw = cryptocompare.get_price(self.crypto_type,self.cash_type)
        price_pure = price_raw[self.crypto_type][self.cash_type]
        self.price = price_pure
        return price_pure

    def num_calculator(self):

        self.crypto_num = self.cash / self.price
        return self.crypto_num

class log:
    def __init__(self,crypto_num,crypto_type,cash_amount,file_directory):
        self.crypto_num = crypto_num
        self.crypto_type = crypto_type
        self.cash_amount= cash_amount
        self.file_directory = file_directory

    def logger(self):
        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y %H:%M:%S")
        output = date_string + " sent " + self.crypto_num + " of " + self.crypto_type + " (" + self.cash_amount + ")"

        try:
            with open(self.file_directory) as r:
                pass
        except FileNotFoundError:
            with open(self.file_directory) as w:
                pass
        logging.info(output)
