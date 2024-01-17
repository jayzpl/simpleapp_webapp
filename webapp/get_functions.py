import requests

def price(symbol: str) -> dict:
    api_url = f'https://min-api.cryptocompare.com/data/generateAvg?fsym={symbol}&tsym=USD&e=coinbase'
    response = requests.get(api_url)
    data = response.json()
    return data