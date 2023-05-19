import numpy
list1, N_and_M = [], list(map(int, input().split()))
for i in range(N_and_M[0]):
    arr = list(map(int, input().split()))
    list1.append(arr)

my_array = numpy.array(list1)
print(numpy.transpose(my_array), my_array.flatten(), sep="\n")

"""
sample input
2 2
1 2
3 4
"""