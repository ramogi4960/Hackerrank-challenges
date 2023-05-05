# in this challenge, we first take in an int N, representing the first N fibonacci numbers
# we are supposed to print out the cube of each number in the fibonacci list
cube = lambda x: pow(x, 3) # complete the lambda function


def fibonacci(n):
    fib = [0, 1]
    if n == 0:
        fib.clear()
    elif n == 1:
        fib = [0, ]
    else:
        for i in range(2, n):
            fib.append(sum(fib[i - 2:i]))
    return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))