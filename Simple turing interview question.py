import re

# given a string S, return the "reversed" verion of S such that all non-letters remain in the ssame position
# while the letters are reversed
"""
input: ab-cd
output: dc-ba

input: a-bC-dEf=ghlj!!
output: j-lh-gfE=dCba!!
"""
pattern = re.compile(r"[A-Za-z]")


def reverse(s: str) -> str:
    letters, final = [], ""
    for i in s:
        if pattern.match(i):
            letters.append(i)
        else:
            pass
    for item in s:
        if pattern.match(item):
            final += letters[-1]
            letters.pop()
        else:
            final += item

    return final


print(reverse(input("Enter string: ")))
