# Block development using web3

""" >>> from web3 import Web3

# IPCProvider:
>>> w3 = Web3(Web3.IPCProvider('./path/to/geth.ipc'))

# HTTPProvider:
>>> w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# WebsocketProvider:
>>> w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))

>>> w3.isConnected()
True """

from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<infura-project-id>'))

from web3.auto.infura import w3

print (w3.eth.block_number)
