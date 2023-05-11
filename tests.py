import re
word = """
I went to the zoo, I saw a fat monkey and I thought it was you
You should have seen it
I'm a youth man
"""
b = "aaabaab"
c = "aa"
pat = re.compile(c)
list1 = []
for i in range(len(b)):
    y = b[i:]
    if pat.match(y) is None:
        pass
    else:
        l = pat.match(y)
        list1.append([i, (i+len(c))-1])


print(list1)


