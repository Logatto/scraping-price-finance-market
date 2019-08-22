from flask import request
import json

from scraping.currency_scraper import currency_scraper


def configure_routes(app):

    @app.route('/')
    def init_route():
        return 'Hello, World'

    @app.route('/api/currencies', methods=['GET'])
    def get_currencies():
        currency_scraper()

        data = {
            'status' : True,
            'data': [
                {'symbol': 'USDEUR'},
                {'symbol': 'USDJPY'},
            ] 
        }

        return json.dumps(data)