from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()


setup(
name = "pycrypto_tx - IndentErr",
version = "0.1",
license = "MIT",
author = "IndentErr",
description = "Free and easy python cryptocurrency transaction library",
url = "https://github.com/IndentErr/pycrypto_tx",
packages = find_packages(),
install_requires = ["cryptocompare","datetime","logging","web3"],
python_version = ">=3.6",
long_description=open('README.md').read(),

)