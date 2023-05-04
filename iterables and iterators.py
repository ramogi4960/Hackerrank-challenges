# we are an int N, a split() string and another int K
from itertools import permutations, combinations

N, arr, K, num_arr = int(input()), input().split(), int(input()), []
for i in range(len(arr)):
    if arr[i] == 'a':
        num_arr.append(i + 1)

count = 0
for i in combinations(range(1, N + 1), K):
    if len(set(i).intersection(set(num_arr))) > 0:
        count += 1

list1 = list(combinations(range(1, N+1), K))
print(round(count/len(list1), 3))

