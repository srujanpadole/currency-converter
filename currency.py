import requests

API_KEY = 'ENTER YOUR API'
BASE_URL = f"ENTER YOUR API={API_KEY}"

CURRENCIES = ["USD","INR","CAD","EUR","AUD","CNY","RUB"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except:
        print("invalide currencies")
        return None

while True:    
    base = input("enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    if base not in  CURRENCIES:
        print("invalade currencies ")
        continue

    try:
        amount = float(input("the amount is :"))
    except ValueError:
        print("number")
        continue


    data = convert_currency(base)
    if not data:
        continue

  
    del data [base]

    print(f"the amount {amount} {base}:")
    for ticker,value in data.items():
       converted= round(value*amount,2)
       print(f"{ticker}:{converted}")


