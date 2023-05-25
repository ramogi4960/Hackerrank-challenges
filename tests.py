import re
pattern = r"(b)?o\1"
print(str(bool(re.match(pattern, input()))).lower())