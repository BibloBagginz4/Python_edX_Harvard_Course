"""
(Written by Jeff Truesdell 12-09-2025)
This is a program that:
    1)  Expects the user to specify as a command-line argument the
        number of Bitcoins, 𝑛, that they would like to buy.
    2)  If that argument cannot be converted to a float, the program
        should exit via sys.exit with an error message.
    3)  It queries the API for the CoinCap Bitcoin Price Index at
        rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey.
    4)  You should replace YourApiKey with the actual API key you
        obtained from your CoinCap account dashboard, which returns a
        JSON object, among whose nested keys is the current price of
        Bitcoin as a float.
    5)  All exceptions will be caught, as with code like:
            import requests
            try:
            except requests.RequestException:
    6)  Outputs the current cost of 𝑛 Bitcoins in USD to four decimal
        places, using comma "," as a thousands separator.
"""

import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            num_coins = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

    price = num_coins * get_coin_price()
    print(f"${price:,.4f}")


def get_coin_price():
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=d3fba6e6eb86097270bfea84e187e8a74df464f84e9de67b8bb440169060d6cf"
        )
        response.raise_for_status()  # Check for errors
        content = response.json()
        coin_price = float(content["data"]["priceUsd"])
    except requests.HTTPError:
        sys.exit("Couldn't complete request!")

    return coin_price


if __name__ == "__main__":
    main()
