# in this tas, we are given an integer n and we are supposed to find the maximum number of consecutive 1's of it's
# binary form
import re
if __name__ == "__main__":
    n = int(input())

b, pattern, count = str(bin(n))[2:], re.compile(r"11+"), 1
if pattern.search(b):
    for item in list(pattern.findall(b)):
        if len(item) >= count:
            count = len(item)
        else:
            pass
print(count)