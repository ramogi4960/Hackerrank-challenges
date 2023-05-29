from functools import reduce
l = [2, 4, 9]
t = list(reduce(lambda x, y: x*y, l))
print(t)