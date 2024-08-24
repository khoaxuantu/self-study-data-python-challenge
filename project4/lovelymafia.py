# %%
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import time

# %%
def scrape_data(name):
    '''
    Scrape data from coinmarketcap.com for a given cryptocurrency.
    Args:
        name (str): The name of the cryptocurrency to scrape data for.
    Returns:
        dict: A dictionary containing the following keys:
            - 'Crypto name' (str): The name of the cryptocurrency.
            - 'price' (float): The current price of the cryptocurrency.
            - 'pct_1d' (float): The percentage change in price over the last 24 hours (1 day).
            - 'pct_7d' (float): The percentage change in price over the last 7 days.
            - 'market_cap' (float): The market capitalization of the cryptocurrency.
            - 'vol_24h' (float): The 24-hour trading volume of the cryptocurrency.
            - 'time_stamp' (str): The timestamp when the data was scraped
    '''

    def price_clean_and_convert(value_str, currency_str='$', split_str=','):
        '''
        Clean and convert the price value.
        Args:
            value_str (str): The price value as a string.
            currency_str (str): The currency symbol to remove from the string.
            split_str (str): The string to split the value on.
        Returns:
            float: The cleaned and converted price value.
        '''
        return float(value_str.replace(split_str, '').replace(currency_str, ''))

    def pct_clean_and_convert(value_str, soup):
        '''
        Clean and convert the percentage value.
        Args:
            value_str (str): The percentage value as a string.
            soup (BeautifulSoup): The BeautifulSoup object for the page.
        Returns:
            float: The cleaned and converted percentage value.
        '''
        pct = float(value_str.split('%')[0])
        if soup['data-change'] == 'down':
            pct = -pct
        return pct

    url = f'https://coinmarketcap.com/currencies/{name}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price = soup.find('span', class_='sc-65e7f566-0 clvjgF base-text').text
    price = price_clean_and_convert(price, currency_str='$', split_str=',')
    pct_1d = soup.find(
        'p', class_='sc-71024e3e-0 sc-58c82cf9-1 bgxfSG iPawMI').text
    pct_1d = pct_clean_and_convert(pct_1d, soup.find(
        'p', class_='sc-71024e3e-0 sc-58c82cf9-1 bgxfSG iPawMI'))
    pct_7d = soup.find(
        'p', class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI').text
    pct_7d = pct_clean_and_convert(pct_7d, soup.find(
        'p', class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI'))
    metrics = soup.find_all('dd', class_='sc-65e7f566-0 dzgtSD base-text')
    market_cap = metrics[0].text.split('%')[1]
    market_cap = price_clean_and_convert(
        market_cap, currency_str='$', split_str=',')
    vol_24h = metrics[1].text.split('%')[1]
    vol_24h = price_clean_and_convert(vol_24h, currency_str='$', split_str=',')

    return {
        'Crypto name': name,
        'price': price,
        'pct_1d': pct_1d,
        'pct_7d': pct_7d,
        'market_cap': market_cap,
        'vol_24h': vol_24h,
        'time_stamp': datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    }


def scrape_data_to_csv(name, period=5, iter=10):
    '''
    Scrape data from coinmarketcap.com for a given cryptocurrency and save it to a CSV file.
    Args:
        name (str): The name of the cryptocurrency to scrape data for.
        period (int): The time in seconds to wait between scraping requests. Default is 5 seconds.
        iter (int): The number of times to scrape data. Default is 10.
    Returns:
        pd.DataFrame: A DataFrame containing the scraped data.
    '''
    data = []
    for i in range(iter):
        data.append(scrape_data(name))
        time.sleep(period)
    df = pd.DataFrame(data)
    return df

# %%
btc_df = scrape_data_to_csv('bitcoin', period=1, iter=10)

# %%
ethereum_df = scrape_data_to_csv('ethereum', period=1, iter=10)

# %%
bnb_df = scrape_data_to_csv('bnb', period=1, iter=10)