# src/main.py
from market_orders import place_market_order
from limit_orders import place_limit_order
from validators import *

def main():
    print("Choose order type:")
    print("1. Market Order")
    print("2. Limit Order")

    choice = input("Enter choice: ")

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    if not is_valid_symbol(symbol):
        print("Invalid symbol format!")
        return

    side = input("Enter side (BUY/SELL): ").upper()
    if not is_valid_side(side):
        print("Invalid side. Use BUY or SELL.")
        return

    quantity = input("Enter quantity: ")
    if not is_valid_quantity(quantity):
        print("Invalid quantity.")
        return
    quantity = float(quantity)

    if choice == '1':
        place_market_order(symbol, side, quantity)

    elif choice == '2':
        price = input("Enter limit price: ")
        if not is_valid_price(price):
            print("Invalid price.")
            return
        price = float(price)
        place_limit_order(symbol, side, quantity, price)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
