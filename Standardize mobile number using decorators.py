# in this task, we are supposed to use decorators to standardize mobile numbers
# We are supposed to print the mobile numbers in the format +91 xxxxx xxxxx, where the x's represent the 10 digit num
# the input numbers can either start with 0, 91, +91, or just the 10 digit number without a prefix

def wrapper(f): # the decorator function that takes a function as an argument
    def fun(l):
        a = f(l)
        
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


