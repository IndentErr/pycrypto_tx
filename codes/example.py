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

price = price_calculation()
num = num_calculation(price)

print(price)
print(num)