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


