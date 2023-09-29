import requests
import sys


if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])

    except:
        sys.exit("Command-line argument is not a number")

else:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    response = r.json()
    bitcoin = (response["bpi"]["USD"]["rate_float"])
    total_amount = bitcoin * amount
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    sys.exit("RequestExceptional")
