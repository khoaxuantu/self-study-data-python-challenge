### IMPORTANT: You must have all these modules installed in your working environment before running the code.
import schedule
import time

# Switch this cancel flag to True to cancel the job
cancel_flag = False

# Here is the file path you want the result csv file to be in.
# The file path must be a raw string, or be left blank if you want it to be created in your current working directory.
# Use front slashes instead of backslashes for the file path. It must end with a front slash.
file_path = r'C:/Users/admin/OneDrive/Documents/Python_practice/Project 4/'

def automated_crypto_scraping(file_path=''):
    '''
    Allows automated web scraping from https://coinmarketcap.com.
    This function will create a csv file in your chosen file path and append new data to it every 10 seconds, until the job is cancelled.
    '''
    try:            
        # Import statements
        from bs4 import BeautifulSoup
        import requests
        import pandas as pd
        from datetime import datetime as dt
        import re
        import os
        
        # Scrape raw data and retrieve current timestamp
        url = 'https://coinmarketcap.com'
        page = requests.get(url)
        time_stamp = dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        table = BeautifulSoup(page.text, 'html').find('table', class_='sc-7b3ac367-3 etbcea cmc-table')
    
        # Leave out the first, second and last columns as they're unnecessary
        column_names = table.find_all('th')
        columns = [column.text for column in column_names[2:-1]]
        
        # Create a temporary dataframe
        df = pd.DataFrame(columns=columns+['Timestamp'])
        
        # Function for data cleaning
        def data_cleaner(df):
            '''A custom function that cleans data scraped from https://coinmarketcap.com.'''
            # Remove the ticker symbol and the dollar signs out of the 'Name' and 'Circulating Supply' columns
            df['Name'] = df['Name'].str[:-3]
            df['Circulating Supply'] = df['Circulating Supply'].str[:-4].str.replace(',', '', regex=False).astype('int')
            
            # The Volume(24h) column needs to be split into 2 new columns: value in USD and volume of the currency traded
            def split_volume(volume_str):
                split_index = None
                for i, char in enumerate(volume_str):
                    # If a fourth digit after a comma is detected, let that digit be the splitting point
                    if char == ',' and volume_str[i+4].isdigit():
                        split_index = i+4
                        break
                if split_index is None:
                    return None, None
                else:
                    usd_value = int(volume_str[1:split_index].replace(',', ''))
                    cur_volume = int(volume_str[split_index:-4].replace(',', ''))
                    return usd_value, cur_volume
        
            df[['Volume(24h)_USD', 'Volume(24h)_Currency']] = df['Volume(24h)'].apply(lambda x: pd.Series(split_volume(x)))
            df.drop(columns=['Volume(24h)'], inplace=True) # Remove the original column after use
        
            # Remove $ and , from the 'Price' column
            df['Price'] = df['Price'].str[1:].str.replace(',', '', regex=False).astype('float')
            # Remove %
            percent_columns = ['1h %', '24h %', '7d %']
            for column in percent_columns:
                df[column] = df[column].str[:-1].astype('float')
            
            # Clean the 'Market Cap' column
            def marcap_clean(text):
                parts = text.split('$')
                if len(parts) >= 3:
                    digits = parts[2]
                    return int(re.sub(r'[,\D]', '', digits))
                else:
                    return None
        
            df['Market Cap'] = df['Market Cap'].apply(marcap_clean)
            
            # Return the cleaned dataframe
            return df
    
        # Define a list of currencies we are interested in
        currency_list = ['Bitcoin', 'Ethereum', 'BNB']
        # Retrieve data rows
        rows = table.find_all('tr', {'style': 'cursor:pointer'})
        for row in rows:
            row_data = row.find_all('td')
            individual_data = [data.text for data in row_data[2:-1]]
            if individual_data[0][:-3] in currency_list:
                # Adding the current timestamp to the list
                individual_data.append(time_stamp)
                # Adding data to the df
                length = len(df)
                df.loc[length] = individual_data
        df = data_cleaner(df)
        # Append the result df to a csv file
        if not os.path.exists(file_path + 'crypto_scraped_data.csv'):
            df.to_csv(file_path + 'crypto_scraped_data.csv', index=False)
        else:
            df.to_csv(file_path + 'crypto_scraped_data.csv', mode='a', header=False, index=False)
    
        # Notify that the function is running
        print('Scraping in process...')
    except Exception as e:
        print(e)

# Define a job
def job():
    if not cancel_flag:
        automated_crypto_scraping(file_path)

# Schedule the function to run every 10 seconds
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    if cancel_flag:
        break
