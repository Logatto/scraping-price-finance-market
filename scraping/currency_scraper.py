import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

from models.currency import Currency



def currency_scraper():
    url = 'https://finance.yahoo.com/currencies'
    
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html.parser")
    
    symbol = bsObj.find_all('a', {'class': 'Fw(b)'})
    
    print(symbol)