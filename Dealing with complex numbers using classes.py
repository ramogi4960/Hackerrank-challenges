import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.complex = complex(real, imaginary)
        self.real = self.complex.real
        self.imaginary = self.complex.imag

    def __add__(self, no):
        result = self.complex + complex(no.real, no.imaginary)
        return complex(result.real, result.imag)

    def __sub__(self, no):
        result = self.complex - complex(no.real, no.imaginary)
        return complex(result.real, result.imag)

    def __mul__(self, no):
        result = self.complex * complex(no.real, no.imaginary)
        return complex(result.real, result.imag)

    def __truediv__(self, no):
        result = self.complex / complex(no.real, no.imaginary)
        return complex(result.real, result.imag)

    def mod(self):
        result = abs(self.complex)
        return complex(result.real, result.imag)

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

"""
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.complex = complex(real, imaginary)
        self.real = self.complex.real
        self.imaginary = self.complex.imag
    def __add__(self, no):
        res = self.complex + complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)
    def __sub__(self, no):
        res = self.complex - complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)
    def __mul__(self, no):
        res = self.complex * complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)
    def __truediv__(self, no):
        res = self.complex / complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)
    def mod(self):
        res = abs(self.complex)

        return Complex(res.real, res.imag)
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
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
"""
