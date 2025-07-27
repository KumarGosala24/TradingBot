# src/advanced/oco.py
from binance_client import client
from loguru import logger

logger.add("../bot.log", rotation="1 MB")

def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price):
    try:
        opposite_side = "SELL" if side == "BUY" else "BUY"

        # Take profit order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type="TAKE_PROFIT_MARKET",
            stopPrice=take_profit_price,
            quantity=quantity,
            reduceOnly=True
        )

        # Stop loss order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=opposite_side,
            type="STOP_MARKET",
            stopPrice=stop_loss_price,
            quantity=quantity,
            reduceOnly=True
        )

        logger.info(f"OCO order placed: TP={tp_order}, SL={sl_order}")
        return tp_order, sl_order
    except Exception as e:
        logger.error(f"OCO order failed: {e}")
        return None
