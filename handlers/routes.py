from flask import request, Response
import json

from scraping.currency_scraper import currencies_scraper, currency_scraper


def configure_routes(app):

    @app.route('/')
    def init_route():
        return 'Hello, World'

    @app.route('/api/currencies', methods=['GET'])
    def get_currencies():

        data = {
            'status' : True,
            'data': currencies_scraper()
        }

        response = Response(json.dumps(data), mimetype='application/json')

        return response

    @app.route('/api/currency/<symbol_text>', methods=['GET'])
    def get_currency(symbol_text):
        
        data = {
            'status' : True,
            'data': currency_scraper(symbol_text)
        }

        response = Response(json.dumps(data), mimetype='application/json')

        return response