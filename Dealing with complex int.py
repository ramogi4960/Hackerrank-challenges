# the task here is to print operation results of two complex numbers
# these complex numbers are first inputed as a string, and then we have to convert them into a complex number
# complex numbers have a real and imaginary part, A and B respectively
# if B<0, then the complex number is A-Bi
# if A or B is 0, then it should be 0.00+Bi or A+0.00i respectively
# we can do this by first defining a function to take care of the conditions and converts the input into a complex number
# then we can print out results of the operations vertically

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.complex = complex(real, imaginary)
        self.real = complex.real
        self.imaginary = complex.imaginary

    def __add__(self, no):
        result = 
    def __sub__(self, no):

    def __mul__(self, no):

    def __truediv__(self, no):

    def mod(self):

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')