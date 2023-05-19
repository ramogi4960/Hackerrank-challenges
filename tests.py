def square(fun):
    def inner(num):
        print("this is the result")
        print(fun(num))

    return inner


@square
def outer(s):
    print(s ** 2)


x = square(outer)
x(5)