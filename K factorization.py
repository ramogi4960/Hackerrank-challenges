import math
from itertools import combinations, combinations_with_replacement
N, K, = map(int, input().split())
number_list = list(map(int, input().split()))
yes, no = [], {-1, }
for i in range(1, K+1):
    for item in list(combinations(number_list, i)):
        if math.prod(item) == N:
            yes.append(item)
        else:
            no.add(-1)

if not yes:
    print(*no)
else:
    p = [1, ]
    for i in yes[0]:
        p.append(i * p[-1])
    print(*p, sep=" ")