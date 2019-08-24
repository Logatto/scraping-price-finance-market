from flask import request, Response
import json

from scraping.currency_scraper import currencies_scraper, currency_scraper


def configure_routes(app):

    @app.route('/')
    def init_route():
        return 'Hello, World'

    @app.route('/api/currencies', methods=['GET'])
    def get_currencies():

        currencies = currencies_scraper()

        data = {
            'status' : True if len(currencies) > 0 else False,
            'data': currencies
        }

        response = Response(json.dumps(data), mimetype='application/json')

        return response

    @app.route('/api/currencies/<symbol_text>', methods=['GET'])
    def get_currency(symbol_text):
        
        currency = currency_scraper(symbol_text)

        data = {
            'status' : True if len(currency) > 0 else False ,
            'data': currency
        }

        response = Response(json.dumps(data), mimetype='application/json')

        return response