from bcolors import bcolors
from bitstamp import api, sell, buy, transaction_fee, currency_pair


print(bcolors.OKGREEN + "Select Currency Pair." + bcolors.ENDC)
print(bcolors.WARNING + ','.join(currency_pair) + bcolors.ENDC)


choice = input("Enter choice [btcusd]:") or "btcusd" 

if choice in currency_pair:

    operation = input("operation you want to do? buy/sell [buy]: ") or "buy".lower() 

    if operation == 'sell':

        # getting the currency separately Ex. BTCUSD > ['BTC', 'USD']

        currency_pair = [choice[0:3].upper(), choice[3:6].upper()]

        # the amount we want to sell

        amount = float(input("Enter Amount (" + currency_pair[0] + "): "))

        # requesting api with our selected currency pair

        currency_pair_amount = api.getJSON(choice)

        # detecting if the api responded well to our request

        if currency_pair_amount:

            # print transaction

            print(bcolors.OKGREEN + "Sell price: " + currency_pair_amount['ask'] + bcolors.ENDC)
            print(bcolors.OKGREEN + "Fee: " + str(transaction_fee) + "%" + bcolors.ENDC)
            print(bcolors.OKGREEN + "Total: " + currency_pair[1] + " " + sell(amount, float(currency_pair_amount['ask'])) + bcolors.ENDC)

        else:

            print(bcolors.FAIL + "Bitstamp API Error" + bcolors.ENDC)


    else:

        currency_pair = [choice[0:3].upper(), choice[3:6].upper()]
       

        amount = float(input("Enter Amount (" + currency_pair[1] + "): "))

        currency_pair_amount = api.getJSON(choice)

        if currency_pair_amount:

            print(bcolors.OKGREEN + "PURCHASE PRICE: " + currency_pair_amount['ask'] + bcolors.ENDC)
            print(bcolors.OKGREEN + "TRANSACTION FEE: " + str(transaction_fee) + bcolors.ENDC)
            print(bcolors.OKGREEN + "YOU GET: " + currency_pair[0] + " " + buy(amount, float(currency_pair_amount['ask'])) + bcolors.ENDC)

        else:

            print(bcolors.FAIL + "Bitstamp API Error" + bcolors.ENDC)
            
else:
    print(bcolors.FAIL + "Currency Pair does not exist" + bcolors.ENDC)    