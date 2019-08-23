import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

from models.currency import Currency



def currency_scraper():
    url = 'https://finance.yahoo.com/currencies'
    
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")
    
    data = []

    symbols = bsObj.find_all('a', {'class': 'Fw(b)'})

    for symbol in symbols:
        cast_currency = Currency(symbol.get('title'), symbol.text)
        data.append(cast_currency.__dict__)
    
    return data