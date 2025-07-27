# src/validators.py

def is_valid_symbol(symbol):
    return symbol.endswith("USDT") and symbol.isalnum()

def is_valid_side(side):
    return side in ["BUY", "SELL"]

def is_valid_quantity(quantity):
    try:
        return float(quantity) > 0
    except ValueError:
        return False

def is_valid_price(price):
    try:
        return float(price) > 0
    except ValueError:
        return False
