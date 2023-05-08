# in this task, we are supposed to print out the first character of a given string that repeats
# the character must be alphanumerical.
# we can do this by first using a findall() function to place all alphanumerical characters into a list
# we can find the first occurrence of repetition by using a conditional statement that compares
# the character to the one after it
import re
"""Without group() function"""
# alnum_list = re.findall(r"[a-zA-Z0-9]", input())
# for i in range(len(alnum_list)-1):
#     if alnum_list[i] == alnum_list[i+1]:
#         print(alnum_list[i])
#         break
#     elif alnum_list[i] != alnum_list[i+1]:
#         if i == len(alnum_list)-2:
#             print("-1")

"""Using the group() function"""

regex = re.search(r"([0-9a-zA-Z])\1+", input())
print(regex.group(1)) if regex is not None else print("-1")