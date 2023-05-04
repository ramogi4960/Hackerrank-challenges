from collections import deque
n, d = int(input()), deque()
for i in range(n):
    command = input().split()
    if len(command) > 1:
        word, value = command[0], int(command[1])
    else:
        word = command[0]
    if word == "append":
        d.append(value)
    elif word == "appendleft":
        d.appendleft(value)
    elif word == "pop":
        d.pop()
    elif word == "popleft":
        d.popleft()

print(*d)