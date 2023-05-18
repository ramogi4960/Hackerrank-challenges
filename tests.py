import re

"""
1
x&& &&& && && x || | ||\|| x
"""

"""
1
c $&1|| || && && &|&&| & | | &&c
"""

"""
1
n && && && && && &&n
"""
text = """
hello hello
you are it
bye bye
"""
print(re.findall(r"(\w+) \1", text))