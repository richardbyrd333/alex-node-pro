import requests
from .config import ETHERSCAN_API_KEY, THRESHOLD_USD
from .utils import get_eth_price

def get_large_transactions():
    eth_price = get_eth_price()
    url = f"https://api.etherscan.io/api?module=account&action=txlistinternal&startblock=latest&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    txs = response.json()["result"]

    significant_txs = []

    for tx in txs:
        value_eth = int(tx["value"]) / 10**18
        value_usd = value_eth * eth_price
        if value_usd >= THRESHOLD_USD:
            significant_txs.append({
                "from": tx["from"],
                "to": tx["to"],
                "value_usd": value_usd,
                "hash": tx["hash"]
            })

    return significant_txs
