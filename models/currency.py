import json

class Currency():
    def __init__(self, symbol, symbol_text):
        self.symbol = symbol
        self.symbol_text = symbol_text

    def default(self):
        return self
        