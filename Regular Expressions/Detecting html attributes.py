import re
html_lines, l = [input() for _ in range(int(input()))], []
for item in html_lines:
    if re.search(r"(?<=<)[^/].*?(?=>)", item):
        for i in list(re.findall(r"(?<=<)[^/].*?(?=>)", item)):
            l.append(i)

my_dict = {}
for item in l:
    if re.search(r"(?<=\s)\w+(?==)", item):
        b = re.match(r"\w+", item).group()
        if b in my_dict.keys():
            for i in list(re.findall(r"(?<=\s)\w+?(?==)", item)):
                if i in my_dict[b]:
                    pass
                else:
                    my_dict[b].append(i)
        else:
            my_dict[b] = []
            for i in list(re.findall(r"(?<=\s)\w+?(?==)", item)):
                my_dict[b].append(i)
    else:
        my_dict[item] = []

x = []
for item in my_dict.keys():
    a = []
    if not my_dict[item]:
        a.append(item)
    else:
        a.append(item)
        a.append(my_dict[item])
    x.append(a)


for item in sorted(x):
    if len(item) == 1:
        print(item[0]+":")
    else:
        a = item[0]
        b = ",".join(sorted(item[1]))
        print(a+":"+b)