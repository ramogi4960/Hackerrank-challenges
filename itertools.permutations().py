# first we are given a string and an integer. We convert the string into uppercase then into lexicographic order
# then we use permutations with the integer as the specified range of the permutations, to find all the permutations
# finally, we print the permutations vertically by printing through iterations of each element in the permutations list
from itertools import permutations
string = input().split()
S = sorted(string[0].upper())
r = int(string[1])

for i in range(len(list(permutations(S, r)))):
    m = ''
    p = list(permutations(S, r))[i]
    for n in p:
        m += n
    print(m)
    