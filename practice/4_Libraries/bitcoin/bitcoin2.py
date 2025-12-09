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

import sys
import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
API_KEY = "your_api_key_here"


def main():
    # Validate command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get price
    price_usd = get_coin_price()
    total = num_coins * price_usd

    print(f"${total:,.4f}")


def get_coin_price():
    try:
        response = requests.get(API_URL, params={"apiKey": API_KEY})
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Couldn't complete request!")
