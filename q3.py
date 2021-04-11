# Python3 Program to find
# best buying and selling days

def productBuySell(price, n):
    if price!=sorted(price,reverse=True):
        low=price[0]
        high=price[1]
        for i in price:
            if i<low:low=i
            if i>high:high=i

        print("Buy on day: ", price.index(low)+1, "\t",
              "Sell on day: ", price.index(high)+1)



# Driver code

# product prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Fucntion call
productBuySell(price, n)
