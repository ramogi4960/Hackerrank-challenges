from collections import OrderedDict
N = int(input())
items_prices = OrderedDict()
prices_list = []
for i in range(N):
    enter_item = input().split()
    price = int(enter_item[-1])
    name = ""
    if len(enter_item) > 2:
        name = " ".join(enter_item[0:-1])
    else:
        name = enter_item[0]

    if name in items_prices.keys():
        items_prices[name] += price
    else:
        items_prices[name] = price

for i in items_prices.items():
    print(i[0],i[1])