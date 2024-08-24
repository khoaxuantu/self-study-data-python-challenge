import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_crypto_data(soup):
    crypto_data_list = []
    
    # Find all cryptocurrency rows
    crypto_rows = soup.find_all('div', class_='sc-7b3ac367-2 cFnHu')  # Adjust class name as needed

    for row in crypto_rows:
        try:
            # Extract the cryptocurrency name
            crypto_name_element = row.find('p', class_='sc-71024e3e-0 ehyBa-d')
            crypto_name = crypto_name_element.text.strip() if crypto_name_element else 'N/A'
            
            # Extract the price
            price_element = row.find('div', class_='sc-b3fc6b7-0 dzgUIj')
            price = price_element.text.strip() if price_element else 'N/A'
            
            # Extract the percentage changes
            change_elements = row.find_all('span', class_='sc-a59753b0-0 cmnujh')
            change_1h = change_elements[0].text.strip()
            change_24h = change_elements[1].text.strip()
            change_7d = change_elements[2].text.strip()
            
            # Extract the market cap
            market_cap_element = row.find('span', class_='sc-11478e5d-1 jfwGHx')
            market_cap = market_cap_element.text.strip() if market_cap_element else 'N/A'
            
            # Extract the 24h volume
            volume_24h_element = row.find('p', class_='sc-71024e3e-0 bbHOdE font_weight_500')
            volume_24h = volume_24h_element.text.strip() if volume_24h_element else 'N/A'
            
            # Create a dictionary with the extracted data
            crypto_data = {
                'Crypto Name': crypto_name,
                'Price': price,
                '1h %': change_1h,
                '24h %': change_24h,
                '7d %': change_7d,
                'Market Cap': market_cap,
                '24h Volume': volume_24h,
                'Event Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            # Append the dictionary to the list
            crypto_data_list.append(crypto_data)
        
        except AttributeError:
            # Handle cases where an element may not be found
            continue
    
    return crypto_data_list

def scrape_crypto_data():
    url = 'https://coinmarketcap.com/'
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        return parse_crypto_data(soup)
    return []

def main():
    all_crypto_data = scrape_crypto_data()
    
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(all_crypto_data)
    
    # Print the DataFrame
    print(df)

if __name__ == '__main__':
    main()
