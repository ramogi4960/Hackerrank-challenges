import re
N_list = [input() for _ in range(int(input()))]
T_list = [input() for _ in range(int(input()))]
for item in T_list:
    c, count = item[:-2], 0
    pat = re.compile(rf"\b{c}(se|ze)\b")
    for i in N_list:
        if pat.search(i):
            count += len(list(pat.findall(i)))
    print(count)