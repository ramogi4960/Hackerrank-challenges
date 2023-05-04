# we are supposed to output the results of an equation (a**2+b**2+c**2)%M, where
# a, b and c are items from a list A, B, C respectively
# we are supposed to choose only one value from each list. we can get all possible values
# selections using itertools.product()
# after that, we need to check which selection will produce the max result after %M
# we can get the cartesian product of a list's items which are lists of the lists A, B, C...
# for each cartesian product, we can append a nother list with the value of s.max,
# then print out the max value of that list

from itertools import product
K, M = list(map(int, input().split()))
list1 = []
for i in range(K):
    num_and_list = list(map(int, input().split()))
    arr = num_and_list[1:]
    list1.append(arr)

final_list = []
products_list = list(product(*list1))
for p in products_list:
    r = 0
    for item in p:
        a = (pow(item, 2))
        r += a
    final_list.append(r%M)

print(max(final_list))

# final_list = [sum(p**2 for p in i)%M for i in products_list]
# print(max(final_list))

