"""
ID: ********
LANG: PYTHON2
TASK: milk
"""

price_list = []
with open('milk.in','r') as fin:
    amount, farmers = map(int, fin.readline().split())
    for i in range(farmers):
        price, supply = map(int, fin.readline().split())
        price_list.append((price, supply))
#print price_list
price_list.sort() #sorts list by first element of tuples, the prices
#print price_list
#print min(price_list)

minprice = 0
amount_needed = amount
for pair in price_list:
    if amount_needed == 0: #no more milk needed means stop loop
        break
    elif pair[1] <= amount_needed: #more needed than in supply
        minprice += pair[0] * pair[1] #adds price * supply = money paid to total
        amount_needed -= pair[1] #subtracts amount gained from total
    else: #more in supply than needed
        minprice += pair[0] * amount_needed
        amount_needed = 0
        break
fout = open("milk.out", "w")
fout.write(str(minprice) + "\n")
fout.close()
