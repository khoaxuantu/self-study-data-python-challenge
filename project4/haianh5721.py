import requests
import time

def get_crypto_data(crypto_ids):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        'id': ','.join(crypto_ids)
    }
    headers = {
        'X-CMC_PRO_API_KEY': 'b302102e-65a1-4661-9b2f-f5fdcaa2d58b' #thay api key của bạn vào đây
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_crypto_info(crypto_data):
    for id, info in crypto_data.items():
        print(f"{info['name']} ({info['symbol']}):")
        print(f"  Price: ${info['quote']['USD']['price']:,.2f}")
        print(f"  Market Cap: ${info['quote']['USD']['market_cap']:,.0f}")
        print(f"  24h Volume: ${info['quote']['USD']['volume_24h']:,.0f}")
        print(f"  24h Change: {info['quote']['USD']['percent_change_24h']:.2f}%")
        print(f"  Last Updated: {info['last_updated']}")
        print('-' * 50)

def main():
    # ID của Bitcoin, Ethereum, và Binance Coin trên CoinMarketCap
    crypto_ids = ['1', '1027', '1839']
    
    while True:
        data = get_crypto_data(crypto_ids)
        if data:
            display_crypto_info(data)
        else:
            print("Failed to retrieve data")
        
        print("Hãy đợi 30s cho lần cập nhật tới")
        time.sleep(30)

if __name__ == "__main__":
    main()
