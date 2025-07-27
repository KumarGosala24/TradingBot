# src/advanced/grid.py
from binance_client import client
from loguru import logger

logger.add("../bot.log", rotation="1 MB")

def place_grid_orders(symbol, lower_price, upper_price, grid_count, quantity):
    """
    Places alternating limit BUY and SELL orders within a price grid.
    """
    step = (upper_price - lower_price) / (grid_count - 1)
    logger.info(f"Placing Grid Orders from {lower_price} to {upper_price} with {grid_count} levels")

    for i in range(grid_count):
        price = round(lower_price + i * step, 2)

        side = "BUY" if i % 2 == 0 else "SELL"

        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                price=price,
                quantity=quantity,
                timeInForce="GTC"
            )
            logger.info(f"Grid {side} Order {i+1}: {order}")
        except Exception as e:
            logger.error(f"Grid order {i+1} failed: {e}")
