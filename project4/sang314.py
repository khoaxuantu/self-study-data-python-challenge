# You must specify other data points, not us :D.

import requests
from bs4 import BeautifulSoup


def scrape_crypto_data(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Replace placeholders with actual CSS selectors or XPath expressions
    price_element = soup.select_one(".price-value")  # Adjust selector
    price = price_element.text.strip() if price_element else None

    # Similarly, find elements for other data points
    percent_1h_element = soup.select_one(".priceChange1h")  # Adjust selector
    percent_1h = percent_1h_element.text.strip() if percent_1h_element else None

    # ... other data points

    data = {
        "price": price,
        "percent_1h": percent_1h,
        # ... other data points
    }

    return data


# Example usage
bitcoin_url = ""
ethereum_url = ""
bnb_url = ""

bitcoin_data = scrape_crypto_data(bitcoin_url)
ethereum_data = scrape_crypto_data(ethereum_url)
bnb_data = scrape_crypto_data(bnb_url)

print(bitcoin_data)
print(ethereum_data)
print(bnb_data)
