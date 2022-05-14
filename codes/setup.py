from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()


setup(
name = "pycrypto_tx - IndentErr",
version = "0.1Alpha",
license = "MIT",
author = "IndentErr",
description = "Free and easy python cryptocurrency transaction library",
url = "https://github.com/IndentErr/pycrypto_tx",
packages = find_packages(),
install_requires = ["cryptocompare","datetime","logging","web3","secrets","codecs","Crypto.Hash","ecdsa","re","bitcoinlib.wallets","base58","hashlib"],
python_version = ">=3.6",
long_description=open('README.md').read(),
classifiers = ["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",]
)