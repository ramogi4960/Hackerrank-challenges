# we are given an input string S, and a substring k
# if a regex search of k occurs at S, we should print the start and end index of that match
# I can do it easily without using the start() and end() methods

# import re
# s, k = input(), input()
# p, list1 = re.compile(k), []
# for i in range(len(s)):
#     b = s[i:]
#     if p.match(b) is None:
#         pass
#     else:
#         list1.append((i, i+len(k)-1))
#
# if len(list1) == 0:
#     t = (-1, -1)
#     print(t)
# else:
#     print(*list1, sep="\n")

""" Using start() and end() methods """
import re
s, pattern_k = input(), re.compile(input())
if pattern_k.search(s) is None:
    print(-1, -1)
else:
    for i in range(len(s)):
        tuple_print = (pattern_k.search(s).start(), pattern_k.search(s).end()-1)
        print(tuple_print)
        s = s.replace(s[:pattern_k.search(s).end()-1], "."*(pattern_k.search(s).end()-1))
       