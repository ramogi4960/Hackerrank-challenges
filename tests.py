import re
alt = r"([0-9]{1})[0-9]{1}\1"
print(re.findall(alt, input()))