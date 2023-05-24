import re
alt = r"(\d)(?=.\1{1})"
print(re.findall(alt, input()))
