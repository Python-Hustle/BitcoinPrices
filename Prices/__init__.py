import requests
from bs4 import BeautifulSoup

url = 'http://www.google.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def data_extraction():
    try:
        content = requests.get('https://coinmarketcap.com/currencies/bitcoin/markets/', headers=headers)
        content1 = requests.get('https://www.cnbcindonesia.com/market-data/currencies/IDR=/USD-IDR', headers=headers)
    except Exception:
        return None

    if content.status_code == 200:
        print(f"[{content.status_code}] Running program...")

        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {"class": "priceValue"})
        price = result.text

        soup1 = BeautifulSoup(content1.text, 'html.parser')
        result1 = soup1.find('div', {"class": "mark_val"})
        idr = result1

        result, result1 = dict()
        result['price'] = price
        result1['idr'] = idr

        return result
        return result1
    else:
        return None


def show_data(result, result1=None):
    if result is None:
        print("Program failed to run")
        return

    print("------------------------------")
    print("\n[ BITCOIN ]")
    print(f"Price : {result['price']}")
    print(f"IDR : {result1['idr']} Rupiah")

