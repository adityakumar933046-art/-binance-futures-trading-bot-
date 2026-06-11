# CLI code goes here
import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def print_summary(response):
    print("\nORDER RESPONSE")
    print("-" * 40)

    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.qty)

        if order_type == "MARKET":

            response = place_market_order(
                args.symbol,
                side,
                quantity
            )

        else:

            validate_price(args.price)

            response = place_limit_order(
                args.symbol,
                side,
                quantity,
                args.price
            )

        print_summary(response)

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    main()
