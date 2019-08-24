import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

from models.currency import Currency


PAGE_FINANCE_YAHOO = 'https://finance.yahoo.com'


def currencies_scraper():

    try:
    
        url = PAGE_FINANCE_YAHOO + '/currencies'
        
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")
        
        data = []

        symbols = bsObj.find_all('a', {'class': 'Fw(b)'})

        for symbol in symbols:
            cast_currency = Currency(symbol.text, symbol.get('title'))
            data.append(cast_currency.__dict__)
        
        return data
    
    except:
        return []

def currency_scraper(symbol):
    try:
        
        symbol = symbol + Currency.X
        url = PAGE_FINANCE_YAHOO + '/quote/%s' % symbol
        
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")

        value_symbol = bsObj.find('div',{'id' : 'quote-market-notice'}).parent.parent.find_next('span').text
        
        cast_currency = Currency(symbol_text=symbol, current_value=value_symbol)

        return cast_currency.__dict__

    except:
        return {}