from web3 import Web3
from django.conf import settings

web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

private_key = settings.PRIVATE_KEY
sender_address = web3.eth.account.from_key(private_key).address



