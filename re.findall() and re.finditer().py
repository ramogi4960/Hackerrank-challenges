# our task here is to find substrings of a string S that contain 2 or more vowels
# these substrings must lie in between 2 consonants and should only contain vowels
# we can do this by checking if a consonant is followed by consecutive vowels
# we can use regex for this by specifying the pattern in the regex pattern
# concsonants - QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm
# vowels - AEIOUaeiou
# I waaant you too beet
# abaaaboopii
import re
p, matches = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}", []
word = input().split()
if len(word) > 1:
    for item in word:  # this will be a list of matches with a consonant at the start
        if item[-1] in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
            matches.append(re.findall(p, item))
else:
    for r in word:
        if r[-1] in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
            matches.append(re.findall(p, r))
        else:
            matches.append(re.findall(p, r))
            matches[-1].pop()

for item in matches:
    for i in item:
        print(i[1:])