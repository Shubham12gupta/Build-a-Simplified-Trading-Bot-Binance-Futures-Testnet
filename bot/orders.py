from bot.validators import *
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Validation
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        order_data = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"

        logger.info(f"Order Request: {order_data}")

        response = client.place_order(**order_data)

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise