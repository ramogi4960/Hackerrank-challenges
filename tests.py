import re
test = input()
for i in list(re.findall(r"(?<=\s)\w+?(?==)", test)):
    print(i)