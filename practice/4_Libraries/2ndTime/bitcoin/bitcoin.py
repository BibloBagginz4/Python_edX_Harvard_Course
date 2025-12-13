"""
(Written by: Jeff Truesdell 12-12-2025)
This program:
    1) Expects the user to specify a command-line argument for the
       number of Bitcoins, 𝑛, that they would like to buy.
    2) If that argument cannot be converted to a float, the program
       exits via sys.exit with an error message.
    3) If 𝑛 is a valid, it will querie the API for the CoinCap
       Bitcoin Price Index:
       3.1) rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey
       3.2) Replace YourApiKey with the actual API key obtained from
            your CoinCap account dashboard, which returns a JSON object,
            among whose nested keys is the current price of Bitcoin as a
            float.
    5) Outputs the current cost of 𝑛 Bitcoins in USD to four decimal
       places, using ,(comma) as a thousands separator.
"""

import sys
import requests

url = "http://rest.coincap.io/v3/assets/bitcoin?apiKey="
key = "d3fba6e6eb86097270bfea84e187e8a74df464f84e9de67b8bb440169060d6cf"


def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Expected one command-line argument")
    except ValueError:
        sys.exit("Argument must be a number")

    try:
        r = requests.get(f"{url}{key}")
        coin_price = float(r.json()["data"]["priceUsd"])
        value = n * coin_price
        print(f"${value:,.4f}")
    except (KeyError, TypeError):
        sys.exit("Error with url request")


if __name__ == "__main__":
    main()
