from flask import Flask
import json

from handlers.routes import configure_routes

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, World'
    assert response.status_code == 200

def test_get_currencies():
    app = Flask(__name__)
    configure_routes(app)
    app.testing = True
    client = app.test_client()
    url = '/api/currencies'


    response = client.get(url)
    result = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert ("status" in result) == True
    assert ("data" in result) == True


def test_get_currency():
    app = Flask(__name__)
    configure_routes(app)
    app.testing = True
    client = app.test_client()


    # Get All currencies to get the first one
    url_currencies = '/api/currencies'
    response_currencies = client.get(url_currencies)
    result_currencies = json.loads(response_currencies.get_data(as_text=True))

    first_currency = None
    if "data" in result_currencies:
        first_currency = result_currencies["data"][0]


    if first_currency and "symbol_text" in first_currency:

        url = '/api/currency/%s' % first_currency["symbol_text"]

        response = client.get(url)
        result = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert ("status" in result) == True
        assert (
            "data" in result 
            and "symbol_text" in result["data"]
            and result["data"]["symbol_text"] == first_currency["symbol_text"]
            ) == True
        


    else:
        assert False

