from setuptools import setup, find_packages

setup(
name = "pycrypto_tx - IndentErr",
version = "0.1",
license = "MIT",
author = "IndentErr",
description = "Free and easy python cryptocurrency transaction library",
url = "https://github.com/IndentErr/pycrypto_tx",
packages = find_packages(),
install_requires = ["cryptocompare","datetime","web3","cryptodome","ecdsa","bitcoinlib","base58","hashlib"],
python_version = ">=3.6",
)