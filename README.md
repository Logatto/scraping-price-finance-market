# scraping-price-finance-market
Proyecto que hace scraping a https://finance.yahoo.com y muestra los datos de algunas monedas del mercado financiero usando Flask 

Installation
------------
to install requeriments

```console
$ pip install -r requeriments.txt
```


Test
------

to run all unit test

```console
$ pytest tests/
````

Use
------

to run the server

```console
$ python3 app.py
```


Endpoints
-----------

*Get all Currencies*

```
http://127.0.0.1:5000/api/currencies
```

*Get one Currency*

```
http://127.0.0.1:5000/api/currency/USDEUR
```