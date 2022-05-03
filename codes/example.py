import pycrypto_tx

#cash,crypto_num,crypto_type,cash_type
#price_calculator
def price_calculation():
    tx_price_calculator = pycrypto_tx.price(100,0,"ETH","USD")
    price_calc = tx_price_calculator.price_calculator()

    return price_calc

def num_calculation():
    crypto_num_calculator = pycrypto_tx.price(100,0,"ETH","USD")
    num_calc = crypto_num_calculator.num_calculator()
    return num_calc

price = price_calculation()
num = num_calculation()

print(price)
print(num)