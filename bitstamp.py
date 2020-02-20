import json
import requests


# commission that charges bitstamp for each transaction

transaction_fee = 0.5

# values supported by bitstamp source: https://www.bitstamp.net/api/

currency_pair = ["btcusd", "btceur", "eurusd", "xrpusd", "xrpeur", "xrpbtc", "ltcusd", "ltceur", "ltcbtc", "ethusd", "etheur", "ethbtc", "bchusd", "bcheur", "bchbtc"]



class api:

    url = "https://www.bitstamp.net/api/v2/ticker/"

    def getJSON(currency_pair):

      rAPI = requests.get(api.url + currency_pair)

      if rAPI.status_code == 200:
        return rAPI.json()
      else:
        return False



def buy(amount, currency_pair_amount):
  
  final_amount = amount * (100 - transaction_fee) / 100

  return (str(final_amount/currency_pair_amount))

def sell(amount, currency_pair_amount):
  
  final_amount = amount * (100 - transaction_fee) / 100

  return (str(final_amount * currency_pair_amount))