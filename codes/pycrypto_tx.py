import cryptocompare
import datetime
import logging
from web3 import Web3
import secrets
import codecs
import os
from Crypto.Hash import keccak
import ecdsa

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

class wallet:
    
    def __init__(self,wallet_address,wallet_privatekey,wallet_balance,wallet_history,web3_url,public_key):
        self.wallet_address = wallet_address
        self.wallet_privatekey = wallet_privatekey
        self.wallet_balance = wallet_balance
        self.wallet_history = wallet_history
        self.web3 = Web3(Web3.HTTPprovider(web3_url))
        self.public_key = self.public_key

    def check_balance(self):
        
        web3 = self.web3
        wallet = self.wallet_address
        balance = web3.eth.get_balance(wallet)
        self.wallet_balace = balance
        return self.wallet_balance

    def create_private(self):
        curve_order =  0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        
        while True:
            if int(self.wallet_privatekey, 16) < curve_order:
                return self.wallet_privatekey
    
    def create_publickey(self):
        
        private_key_bytes = codecs.decode(self.wallet_privatekey, "hex")
        public_key_bytes =  (ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).get_verifying_key().to_string())

        self.public_key = codecs.encode(public_key_bytes, "hex")
        return self.public_key

    def create_address(self):

        k = keccak.new(digest_bits = 256)
        #under development
        return self.wallet_address