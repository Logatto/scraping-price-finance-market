import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

from models.currency import Currency



def currencies_scraper():
    url = 'https://finance.yahoo.com/currencies'
    
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")
    
    data = []

    symbols = bsObj.find_all('a', {'class': 'Fw(b)'})

    for symbol in symbols:
        cast_currency = Currency(symbol.text, symbol.get('title'))
        data.append(cast_currency.__dict__)
    
    return data

def currency_scraper(symbol):
    url = 'https://finance.yahoo.com/quote/%s' % symbol
    
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")

    value_symbol = bsObj.find('div',{'id' : 'quote-market-notice'}).parent.parent.find_next('span').text
    
    cast_currency = Currency(symbol_text=symbol, current_value=value_symbol)

    return cast_currency.__dict__