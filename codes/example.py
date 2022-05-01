import codes.pycrypto_tx as pycrypto_tx

#cash,crypto_num,crypto_type,cash_type
#price_calculator

tx_price_calculator = pycrypto_tx.price(100,0,"ETH","USD")
price_calc = tx_price_calculator.price_calculator()
print(price_calc)