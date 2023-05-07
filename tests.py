import re
reg_pattern = r"[@.]"
split_email = list(re.split(reg_pattern, input()))
print(split_email)