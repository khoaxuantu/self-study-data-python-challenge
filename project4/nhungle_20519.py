{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 482,
   "id": "361b49e8-d2e9-4536-8c74-d09129490404",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 486,
   "id": "4d46b817-3b3d-4044-b1dc-aa087af143c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://coinmarketcap.com/'\n",
    "\n",
    "page = requests.get(url)\n",
    "\n",
    "soup = BeautifulSoup(page.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
   "id": "b0126ebd-c25a-4973-b720-74554537fdea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume(24h)']"
      ]
     },
     "execution_count": 488,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table = soup.find_all('table', 'sc-7b3ac367-3 etbcea cmc-table')\n",
    "\n",
    "rows = table[0].find_all('th')\n",
    "\n",
    "attrs = [row.text for row in rows[2:9]]\n",
    "\n",
    "attrs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 490,
   "id": "59c5fde2-dd19-431e-9247-b8d8cc8a887e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['',\n",
       " '1',\n",
       " 'BitcoinBTC',\n",
       " '$60,603.50',\n",
       " '0.12%',\n",
       " '0.79%',\n",
       " '0.14%',\n",
       " '$1.2T$1,196,169,936,517',\n",
       " '$20,342,812,656335,677 BTC',\n",
       " '19,738,040 BTC',\n",
       " '']"
      ]
     },
     "execution_count": 490,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# testing data\n",
    "\n",
    "test = table[0].find_all('tr')[1].find_all('td')\n",
    "lst_data = [d.text for d in test]\n",
    "lst_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "id": "a7771903-bbb5-4325-ab3b-5347036d6656",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Bitcoin', '$60,603.50', '0.12%', '0.79%', '0.14%', '$1,196,169,936,517', '$20,342,812,656'], ['Ethereum', '$2,599.59', '0.71%', '0.78%', '11.24%', '$312,717,397,882', '$10,873,611,528'], ['BNB', '$515.01', '0.47%', '2.28%', '2.84%', '$75,169,571,590', '$1,380,436,674']]\n"
     ]
    }
   ],
   "source": [
    "list_data = []\n",
    "\n",
    "data_rows = table[0].find_all('tr')\n",
    "\n",
    "for row in data_rows[1:]:\n",
    "    data_row = row.find_all('td')\n",
    "    name_column = data_row[2].find('p', 'sc-71024e3e-0 ehyBa-d')\n",
    "    \n",
    "    if name_column is not None:\n",
    "        name_column = name_column.text\n",
    "        if name_column in ('Bitcoin', 'Ethereum', 'BNB'):\n",
    "            market_Cap = row.find('span', 'sc-11478e5d-1 jfwGHx')\n",
    "            market_Cap = market_Cap.text\n",
    "\n",
    "            volume = row.find('p', 'sc-71024e3e-0 bbHOdE font_weight_500')\n",
    "            volume = volume.text\n",
    "            data = [name_column] + [data_row.text for data_row in data_row[3:7]] + [market_Cap] + [volume]\n",
    "            list_data.append(data)\n",
    "            \n",
    "print(list_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 494,
   "id": "52e2d697-8b1d-457c-8a85-c25f8c011097",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Price</th>\n",
       "      <th>1h %</th>\n",
       "      <th>24h %</th>\n",
       "      <th>7d %</th>\n",
       "      <th>Market Cap</th>\n",
       "      <th>Volume(24h)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bitcoin</td>\n",
       "      <td>$60,603.50</td>\n",
       "      <td>0.12%</td>\n",
       "      <td>0.79%</td>\n",
       "      <td>0.14%</td>\n",
       "      <td>$1,196,169,936,517</td>\n",
       "      <td>$20,342,812,656</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ethereum</td>\n",
       "      <td>$2,599.59</td>\n",
       "      <td>0.71%</td>\n",
       "      <td>0.78%</td>\n",
       "      <td>11.24%</td>\n",
       "      <td>$312,717,397,882</td>\n",
       "      <td>$10,873,611,528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>BNB</td>\n",
       "      <td>$515.01</td>\n",
       "      <td>0.47%</td>\n",
       "      <td>2.28%</td>\n",
       "      <td>2.84%</td>\n",
       "      <td>$75,169,571,590</td>\n",
       "      <td>$1,380,436,674</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Name       Price   1h %  24h %    7d %          Market Cap  \\\n",
       "0   Bitcoin  $60,603.50  0.12%  0.79%   0.14%  $1,196,169,936,517   \n",
       "1  Ethereum   $2,599.59  0.71%  0.78%  11.24%    $312,717,397,882   \n",
       "2       BNB     $515.01  0.47%  2.28%   2.84%     $75,169,571,590   \n",
       "\n",
       "       Volume(24h)  \n",
       "0  $20,342,812,656  \n",
       "1  $10,873,611,528  \n",
       "2   $1,380,436,674  "
      ]
     },
     "execution_count": 494,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(list_data, columns = attrs)\n",
    "\n",
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
