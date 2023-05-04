from collections import deque
T, bool_list = int(input()), []
for i in range(T):
    n, d = int(input()), deque(list(map(int, input().split())))
    for p in range(n):
        if (d[0] >= d[1] or d[-1] >= d[-2]) and len(d) > 2:
            if d[0] >= d[-1]:
                d.popleft()
            else:
                d.pop()
    if len(d) <= 2:
        bool_list.append("Yes")
    else:
        bool_list.append("No")

for i in bool_list:
    print(i)