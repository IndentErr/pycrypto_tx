import cryptocompare
import datetime
import logging
from web3 import Web3
import secrets
import codecs
import re
from Crypto.Hash import keccak
import ecdsa
from bitcoinlib.wallets import Wallet
from base58 import b58decode
from hashlib import sha256
import os
import random
import time

#class or method under development: wallet_bitcoin.check_history(), wallet_ethereum.check_history()
class trading:
    def __init__(self,crypto_num,url,start_address,start_privatekey,destination_address,wallet,transaction_info):
        self.crypto_num = crypto_num
        self.url = url
        self.start_address = start_address
        self.start_privatekey = start_privatekey
        self.destination_address = destination_address
        self.wallet = wallet
        self.transaction_info = transaction_info
    
    def transaction_eth(self):
        web3 = Web3(Web3.HTTPProvider(self.url))
        nonce = web3.eth.getTransactionCount(self.start_address)
        self.transaction_info = {"nonce":nonce, "to":self.destination_address, "value": web3.toWei(self.crypto_num,"ether"), "gas": 2000000, 'gasPrice': web3.toWei('50', 'gwei')}
        web3.eth.account.sign_transaction(self.transaction_info,self.start_privatekey)

        return self.transaction_info

    def transaction_btc(self):

        #under development
        t = self.wallet.send_to(self.destination_address,self.crypto_num)
        self.transaction_info = t.info()
        return self.transaction_info

class price:

    def __init__(self,cash,crypto_num,crypto_type,cash_type,price):

        self.cash = cash
        self.crypto_num = crypto_num
        self.crypto_type = crypto_type
        self.cash_type = cash_type
        self.price = price
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

class wallet_ethereum:
    
    def __init__(self,wallet_address,wallet_privatekey,wallet_balance,wallet_history,web3_url,public_key,block_num):
        self.wallet_address = wallet_address
        self.wallet_privatekey = wallet_privatekey
        self.wallet_balance = wallet_balance
        self.wallet_history = wallet_history
        self.web3 = Web3(Web3.HTTPprovider(web3_url))
        self.public_key = public_key
        self.block_num = block_num

    def check_balance(self):
        
        web3 = self.web3
        wallet = self.wallet_address
        balance = web3.eth.get_balance(wallet)
        self.wallet_balace = balance
        return self.wallet_balance

    #start of creating wallet
    def create_private(self):
        curve_order =  0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        
        while True:

            self.private_key = secrets.token_hex(32)
            if int(self.wallet_privatekey, 16) < curve_order:
                return self.wallet_privatekey
    
    def create_publickey(self):
        
        private_key_bytes = codecs.decode(self.wallet_privatekey, "hex")
        public_key_bytes =  (ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).get_verifying_key().to_string())

        self.public_key = codecs.encode(public_key_bytes, "hex")
        return self.public_key

    def create_address(self):

        k = keccak.new(digest_bits = 256)
        k.update(codecs.decode(self.public_key,"hex"))
        k_hash = k.hexdigest()
        address = "0x" + k_hash[-40:] # last 20bytes
        self.wallet_address = address

        return self.wallet_address

    def check_address(self):
        #The source code is originated from https://github.com/vgaicuks/ethereum-address/blob/master/ethereum_address/utils.py (Apache 2.0 License)
        if not re.match(r'^(0x)?[0-9a-f]{40}$', self.wallet_address, flags=re.IGNORECASE):
            return False
        
        elif re.match(r'^(0x)?[0-9a-f]{40}$', self.wallet_address) or re.match(r'^(0x)?[0-9A-F]{40}$', self.wallet_address):

            return True
        else:
            return False

    #end of creating wallet

    def check_history(self):

        return self.wallet_history
        
    def check_block(self):

        result = self.web3.eth.get_block(self.block_num)
        
        return result

class wallet_bitcoin:
    
    def __init__(self,wallet_address,wallet_privatekey,wallet_balance,wallet_history,wallet_public_key,wallet_name,wallet):

        self.wallet_address = wallet_address
        self.wallet_privatekey = wallet_privatekey
        self.wallet_balance = wallet_balance
        self.wallet_history = wallet_history
        self.public_key = wallet_public_key
        self.wallet_name = wallet_name
        self.wallet = wallet

    def create_address(self):
        self.wallet = Wallet.create(self.wallet_name)
        key_btc = self.wallet.get_key()
        self.wallet_adress = key_btc.address

        return self.wallet_address

    def check_balance(self):
        self.wallet.scan()
        self.wallet_balance = self.wallet.info()
        
        return self.wallet_balance

    def check_address(self):

        valid = None
        bitcoin_address_decoded = b58decode(self.wallet_address)
        version_plus_payload = bitcoin_address_decoded[:-4]
        checksum_found = bitcoin_address_decoded[-4:]

        #calculate real checksum
        checksum_real = sha256(sha256(version_plus_payload).digest()).digest()[:4]

        address_type = None
        version_prefix = version_plus_payload.hex()[0:8]
        if version_prefix[0:2] == "00":
            address_type = "Bitcoin Address"

        elif version_prefix[0:2] == "05":
            address_type = "Pay-to-Script-Hash Address"

        elif version_prefix[0:2] == "6F":
            address_type = "Bitcoin Testnet Address"

        elif version_prefix[0:2] == "80":
            address_type = "Private Key WIF"

        elif version_prefix[0:4] == "0142":
            address_type = "BIP-38 Encrypted Private Key"

        elif version_prefix[0:8] == "0488B21E":
            address_type = "BIP-32 Extended Public Key"

        else:
            address_type = False

        output = [valid,address_type]

        if checksum_found == checksum_real:
            valid = True
        elif checksum_found != checksum_real:
            valid = False
        else:
            valid = False

        return output
    
    def check_history(self):
        
        return self.wallet_history

class wallet_Tether:
    #Tether shares same blockchain with bitcoin

    def __init__(self,wallet_address,wallet_privatekey,wallet_balance,wallet_history,wallet_public_key,wallet_name,wallet):

        self.wallet_address = wallet_address
        self.wallet_privatekey = wallet_privatekey
        self.wallet_balance = wallet_balance
        self.wallet_history = wallet_history
        self.wallet_public_key = wallet_public_key
        self.wallet_name = wallet_name
        self.wallet = wallet
    
    def create_address(self):

        r = str(os.urandom(32)) \
            + str(random.randrange(2 ** 256)) \
            + str(int(time.time() * 1000000))
    
        r = bytes(r, "utf-8")
        h = hashlib.sha256(r).digest()
        key = "".join("{:02x}".format(y) for y in h)
        
        while True:
            if int(key, 17) < N:
                break 

    def check_balance(self):

        return self.wallet_balance