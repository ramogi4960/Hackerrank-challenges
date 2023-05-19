import numpy

# def arrays(arr):
#     arr = arr[::-1]
#     return numpy.array(arr, float)
#
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)


print(numpy.reshape(numpy.array(list(map(int, input().split()))), (3, 3)))

"""
The shape of an array is a tuple with the number of rows and collumns. (rows, collumns)
If there is only 1 row, it returns (collumns, )
"""