# Order functions go here
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER: {response}")

        return response

    except Exception as e:
        logger.error(str(e))
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT ORDER: {response}")

        return response

    except Exception as e:
        logger.error(str(e))
        raise
