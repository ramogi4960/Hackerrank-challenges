# we first take in an int T, which is the number of strings to be worked on
# then we take in a string N, T times.
# for each string, we must find out if that string is a floating point number
# a floating point number has to have a decimal in the beginning or at any other point.
# the floating point number can begin with - or +, but not both
T, S = int(input()), []
for i in range(T):
    N = input()
    # a floating point number has to have "."
    # we need to set conditions for whether N starts with "+" or "-", or both
    # we also need to check if N has more than one "."
    if "." not in N:
        S.append(False)
    else:
        try:
            b = float(N)
            S.append(True)
        except ValueError as e:
            S.append(False)

print(*S, sep="\n")