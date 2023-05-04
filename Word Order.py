# the problem to be solved here is outputing the number of distinct word, followed by the number of times they appear
# we can do this by creating a list of the words, and then checking the count of the words
# we can also stor the words in an iterable object that does not allow duplicates in order to find distinct words
from collections import Counter
n, words = int(input()), []
for i in range(n):
    f = input()
    words.append(f)

print(len(Counter(words).keys()))
for i in Counter(words).values():
    print(i, end=" ")
