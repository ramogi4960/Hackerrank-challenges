# we can get the frequency of the shoe sizes using the Counter method
# we need to compare the size of a customer with the keys in size_frequency.
# if the size exists, we add the amount to a variable, and reduce the value of te key used
from collections import Counter

shoes_total = int(input())
shoe_sizes = list(map(int, input().split()))
customers = int(input())
size_and_price = []  # the size each customer needs and the price paid for it
sizes_frequency = Counter(shoe_sizes) # dictionary containing the frequency of each size
s = list(sizes_frequency.keys())
total_amount = 0
for i in range(customers):
    p = list(map(int, input().split()))
    for item in p:
        size_and_price.append(item)

for i in range(0, len(size_and_price), 2):
    if size_and_price[i] in s:
        total_amount += size_and_price[i+1]
        sizes_frequency[size_and_price[i]] -= 1
        if sizes_frequency[size_and_price[i]] == 0:
            s.remove(size_and_price[i])

print(total_amount)

