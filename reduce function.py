# in this task, we introduce the reduce function from functools module.
# it functions like a map() or filter(), except it iterates a function of two arguments,
# which performs its operations one after the other pair from left to right
from fractions import Fraction
from functools import reduce


def product(fraction):
    t = reduce(lambda x, y: x * y, fraction)
    return t.numerator, t.denominator


if __name__ == '__main__':
    f = []
    for _ in range(int(input())):
        f.append(Fraction(*map(int, input().split())))
    result = product(f)
    print(*result)
