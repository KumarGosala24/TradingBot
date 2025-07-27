# src/limit_orders.py
from binance_client import client
from loguru import logger

logger.add("../bot.log", rotation="1 MB")

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logger.info(f"Limit order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Limit order failed: {e}")
        return None
