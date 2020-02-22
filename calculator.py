from bcolors import bcolors
from bitstamp import api, sell, buy, transaction_fee, currency_pair


print(bcolors.OKGREEN + "Select Currency Pair." + bcolors.ENDC)
print(bcolors.WARNING + ','.join(currency_pair) + bcolors.ENDC)


choice = input("Enter choice [btcusd]:") or "btcusd" 

if choice in currency_pair:

    print(bcolors.OKGREEN + "Types of operations" + bcolors.ENDC)

    print("0. Buy (market price)")
    print("1. Sell (market price)")
    print("2. Buy and Sell (Profits)")
    
    operation = float(input(bcolors.OKGREEN + "Operation you want to do? [0]: " + bcolors.ENDC) or 0)

    if operation == 0:

        # getting the currency separately Ex. BTCUSD > ['BTC', 'USD']

        currency_pair = [choice[0:3].upper(), choice[3:6].upper()]

        # the amount we want to buy

        amount = float(input("Enter Amount (" + currency_pair[1] + "): "))

         # requesting api with our selected currency pair

        currency_pair_amount = api.getJSON(choice)

        # detecting if the api responded well to our request

        if currency_pair_amount:

            # print transaction

            print(bcolors.OKGREEN + "PURCHASE PRICE: " + currency_pair_amount['ask'] + bcolors.ENDC)
            print(bcolors.OKGREEN + "TRANSACTION FEE: " + str(transaction_fee) + bcolors.ENDC)
            print(bcolors.OKGREEN + "YOU GET: " + currency_pair[0] + " " + buy(amount, float(currency_pair_amount['ask'])) + bcolors.ENDC)

        else:

            print(bcolors.FAIL + "Bitstamp API Error" + bcolors.ENDC)

    elif operation == 2:

        # getting the currency separately Ex. BTCUSD > ['BTC', 'USD']

        currency_pair = [choice[0:3].upper(), choice[3:6].upper()]

        # amount to be invested

        your_investment = float(input("Your money to invest (" + currency_pair[1] + "): "))

        # purchase price
        
        currency_value_buy = input(choice.upper() + " Value (Buy): ") 

        # calculating purchase occupying the buy function

        calculating_purchase = buy(your_investment, float(currency_value_buy))

        # printing the purchase

        print(bcolors.OKGREEN + "You have now: " + currency_pair[0] + " " + calculating_purchase + bcolors.ENDC)

        currency_value_sell = input(choice.upper() + " Value (Sell): ")

        calculating_sale = sell(float(calculating_purchase), float(currency_value_sell))


        print(bcolors.OKGREEN + "You sold: " + currency_pair[0] + " " + calculating_purchase + bcolors.ENDC)
        print(bcolors.OKGREEN + "You get: " + currency_pair[1] + " " + calculating_sale + bcolors.ENDC)

        profit = float(calculating_sale) - float(your_investment)

        print(bcolors.OKGREEN + "You profit: " + currency_pair[1] + " " + str(profit) + bcolors.ENDC)
        


    else:

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
    print(bcolors.FAIL + "Currency Pair does not exist" + bcolors.ENDC)    