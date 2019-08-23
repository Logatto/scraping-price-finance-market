from flask import request, Response
import json

from scraping.currency_scraper import currency_scraper


def configure_routes(app):

    @app.route('/')
    def init_route():
        return 'Hello, World'

    @app.route('/api/currencies', methods=['GET'])
    def get_currencies():

        data = {
            'status' : True,
            'data': currency_scraper()
        }

        response = Response(json.dumps(data), mimetype='application/json')

        return response