# src/advanced/twap.py
import time
from binance_client import client
from loguru import logger

logger.add("../bot.log", rotation="1 MB")

def place_twap_orders(symbol, side, total_quantity, slices, interval_seconds):
    """
    TWAP: Split total_quantity into 'slices' and place one MARKET order every 'interval_seconds'.
    """
    slice_quantity = total_quantity / slices
    logger.info(f"Starting TWAP: {slices} orders of {slice_quantity} {symbol} every {interval_seconds}s")

    for i in range(slices):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=round(slice_quantity, 4)  # Rounded to avoid precision issues
            )
            logger.info(f"TWAP Order {i+1}/{slices} placed: {order}")
        except Exception as e:
            logger.error(f"TWAP Order {i+1} failed: {e}")
        time.sleep(interval_seconds)
