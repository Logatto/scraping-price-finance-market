from flask import request
import json


def configure_routes(app):

    @app.route('/')
    def init_route():
        return 'Hello, World'