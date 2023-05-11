# import re
# word = """
# I went to the zoo, I saw a fat monkey and I thought it was you
# You should have seen it
# I'm a youth man
# """
# b = "aaabaab"
# c = "aa"
# pat = re.compile(c)
# list1 = []
# for i in range(len(b)):
#     y = b[i:]
#     if pat.match(y) is None:
#         pass
#     else:
#         l = pat.match(y)
#         list1.append([i, (i+len(c))-1])
#
#
# print(list1)

""" ..................................................................................................."""

# our task here is to find substrings of a string S that contain 2 or more vowels
# these substrings must lie in between 2 consonants and should only contain vowels
# we can do this by checking if a consonant is followed by consecutive vowels
# we can use regex for this by specifying the pattern in the regex pattern
# concsonants - QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm
# vowels - AEIOUaeiou
# I waaant you too beet
# abaaaboopii
# there is no match here


# import re
# p, matches = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}", []
# word = input().split()
# if len(word) > 1:
#     for item in word:  # this will be a list of matches with a consonant at the start
#         if item[-1] in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
#             matches.append(re.findall(p, item))
# else:
#     for r in word:
#         if r[-1] in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
#             matches.append(re.findall(p, r))
#         else:
#             matches.append(re.findall(p, r))
#             matches[-1].pop()
#
#
# # for i in matches:
# #     if len(i) == 0:
# #         matches.remove(i)
#
# print(matches)
#
# # if len(matches) <= 1:
# #     print("-1")
# # else:
# #     print(i for i in matches)
import re
print(bool(re.findall(r"aa", "Kevin")))
