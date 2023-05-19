# numpy can be used to return an array of zeros or ones, with a specified datatype.
# the default data type of the zeros and ones is float

import numpy
# a, b, c = map(int, input().split())
num = tuple(map(int, input().split()))
print(numpy.zeros(num, dtype=int), numpy.ones(num, dtype=int), sep="\n")
