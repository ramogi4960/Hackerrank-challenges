import math

"""
test cases
3
1000000007
100000003
1000003

10
1000000000
1000000001
1000000002
1000000003
1000000004
1000000005
1000000006
1000000007
1000000008
1000000009
"""
t = int(input())


def isPrime(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'


for i in range(t):
    n = int(input())
    print(isPrime(n))
