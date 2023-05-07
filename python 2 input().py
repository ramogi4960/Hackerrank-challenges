# in python 2, input() == eval(raw_input(prompt))
# in this task, we first take in x, and k
# in the next line, we take in P, which is a mathematical function of x to produce k
# P(x) = k
# we are supposed to print out True if the function gives the correct answer, else we print False
# we can do this by replacing the "x" in function P and finding out if the value == k
x, k = input().split()
p = input()
print(eval(p.replace("x", x)) == int(k))
