# src/market_orders.py
from binance_client import client
from loguru import logger

logger.add("../bot.log", rotation="1 MB")

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Market order failed: {e}")
        return None
