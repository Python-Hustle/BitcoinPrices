import requests
from bs4 import BeautifulSoup

content = requests.get('https://coinmarketcap.com/currencies/bitcoin/markets/')
print(content)

soup = BeautifulSoup(content.text, 'html.parser')
result = soup.find('div', {"class": "priceValue"})


print(result)