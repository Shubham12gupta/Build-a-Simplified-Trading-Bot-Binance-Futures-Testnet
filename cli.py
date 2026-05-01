import click
from bot.client import BinanceFuturesClient
from bot.orders import place_order

@click.command()
@click.option("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
@click.option("--side", required=True, type=click.Choice(["BUY", "SELL"], case_sensitive=False))
@click.option("--order_type", required=True, type=click.Choice(["MARKET", "LIMIT"], case_sensitive=False))
@click.option("--quantity", required=True, type=float)
@click.option("--price", required=False, type=float)

def main(symbol, side, order_type, quantity, price):
    client = BinanceFuturesClient()

    print("\n=== ORDER REQUEST SUMMARY ===")
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Type       : {order_type}")
    print(f"Quantity   : {quantity}")
    if order_type.upper() == "LIMIT":
        print(f"Price      : {price}")

    try:
        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Avg Price      : {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print("\n❌ Order failed!")
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()