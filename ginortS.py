# this task accepts a string S and prints that string in a certain order.
# the string should be alnum
S = input()
lower, upper, digits = sorted([i for i in S if i.islower()]), sorted(
    [i for i in S if i.isupper()]), sorted([i for i in S if i.isdigit()])
odds = sorted([i for i in digits if int(i) % 2 == 1])
evens = sorted([i for i in digits if i not in odds])
print("".join(lower + upper + odds + evens))
