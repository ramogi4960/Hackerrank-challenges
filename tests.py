import re
reg_pattern = r"[,.]"
f = re.split(reg_pattern, "1,000,000.00")
print(f)