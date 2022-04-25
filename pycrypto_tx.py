import cryptocompare
import datetime
from web3 import Web3

class trading:
    def __init__(self,cash,crypto_num,url,start_address,start_privatekey,destination_address):
        self.cash = cash
        self.crypto_num = crypto_num
        self.url = url
        self.start_address = start_address
        self.start_privatekey = start_privatekey
        self.destination_address = destination_address
    
    def transaction(self):
        web3 = Web3(Web3.HTTPProvider(self.url))
        nonce = web3.eth.getTransactionCount(self.address_start)
        transaction_info = {"nonce":nonce, "to":self.destination_address, "value": web3.toWei(self.crypto_num,"ether"), "gas": 2000000, 'gasPrice': web3.toWei('50', 'gwei')}
        transaction_sign = web3.eth.account.sign_transaction(transaction_info,self.start_privatekey)

class price:

    def __init__(self,cash,crypto,crypto_type,cash_type):

        self.cash = cash
        self.crypto = crypto
        self.crypto_type = crypto_type
        self.cash_type = cash_type
        self.price = 0
    def price_calculator(self):
        
        price_raw = cryptocompare.get_price(self.crypto_type,self.cash_type)
        price_pure = price_raw[self.crypto_type][self.cash_type]
        self.price = price_pure
        return price_pure

    def num_calculator(self):

        crypto_num = self.cash / self.price
        return crypto_num