import numpy
# numpy.add/subtract/multiply/divide/floor_divide/mod/power
N, M = map(int, input().split())
arr1, arr2 = [], []
for i in range(N):
    arr = list(map(int, input().split()))
    arr1.append(arr)

for i in range(N):
    arr = list(map(int, input().split()))
    arr2.append(arr)

a, b = numpy.array(arr1), numpy.array(arr2)
print(a+b, a-b, a*b, a//b, a%b, a**b, sep="\n")
