# just like strings, arrays can also be concatenated to form new arrays
import numpy
arr1 = numpy.array([[1, 2, 3], [4, 5, 6]])
arr2 = numpy.array([[7, 8, 9], [10, 11, 12]])
print(numpy.concatenate((arr1, arr2)))
