import pycrypto_tx

#cash, crypto_num, crypto_type, cash_type
def price_calculation():
    #only use crypto_type and cash_type
    tx_price_calculator = pycrypto_tx.price(crypto_type = "ETH", cash_type = "USD", cash = None, crypto_num = None, price = None)
    price_calc = tx_price_calculator.price_calculator()

    return price_calc

def num_calculation(price_input):
    #use cash, price
    crypto_num_calculator = pycrypto_tx.price(cash = 100, price = price_input, crypto_num = None, crypto_type = None, cash_type = None)
    num_calc = crypto_num_calculator.num_calculator()
    return num_calc

def ethereum_trading():
    #sending 2 ethereum
    tx = pycrypto_tx.trading(crypto_num = 2, url = "127.0.0.1/8080",start_address = "your address", start_privatekey = "your privatekey", destination_address = "destination's address", wallet = None, transaction_info = None)
    tx_info = pycrypto_tx.trading.transaction_eth()
    return tx_info

price = price_calculation()
num = num_calculation(price)
transaction = ethereum_trading() #return will be dictionary

print(price)
print(num)
print(transaction)