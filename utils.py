import requests

def get_eth_price():
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    return r.json()["ethereum"]["usd"]
