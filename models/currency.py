import json
from datetime import datetime 

class Currency():

    X = "=X"

    def __init__(self, symbol_text, symbol=None, current_value = None):
        self.symbol_text = symbol_text.replace(self.X, '')
        if(symbol):
            self.symbol = symbol

        if(current_value):
            self.current_value = current_value
            self.date = datetime.now().strftime('%Y-%m-%d %I:%M%:%S')
