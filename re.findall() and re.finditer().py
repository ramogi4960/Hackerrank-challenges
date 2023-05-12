# in this task, we are first given a string
# we are supposed to print all vowels occurring consecutively in between consonants
# if there are no consecutively occurring vowels, we print -1
# we can do this by first defining a re pattern to expose the consecutive vowels
# we can append them into a list then print them out vertically
# concsonants - QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm
# vowels - AEIOUaeiou
import re
s = input().split()
matches, consonants, vowels = [], "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm", "AEIOUaeiou"
pattern = re.compile(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}")
for i in s:
    if i[-1] in consonants and pattern.search(i) is not None:
        f = pattern.findall(i)
        for l in f:
            matches.append(l)
    elif i[-1] in vowels and pattern.search(i) is not None:
        f = pattern.findall(i)
        for l in f:
            matches.append(l)
        matches.pop()


if matches:
    for i in matches:
        print(i[1:])
else:
    print(-1)
