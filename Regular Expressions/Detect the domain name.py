import re
pattern, domains = r"(?<=http://).+?(?=.com)", []
for _ in range(int(input())):
    t = input()
    for item in list(re.findall(pattern, t)):
        domains.append(item)

new_list = []
for item in domains:
    t = item.split(".")
    if t[0] == "www" or t[0] == "ww2":
        del t[0]
        new_list.append(".".join(t))
    else:
        new_list.append(item)

print(*new_list, sep=";")