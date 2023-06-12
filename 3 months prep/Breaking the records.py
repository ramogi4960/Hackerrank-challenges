n, scores = int(input()), list(map(int, input().split()))
a, mini, maxi = [scores[0], ], 0, 0
for i in range(1, n):
    if scores[i] > max(a):
        maxi += 1
        a.append(scores[i])
    elif scores[i] < min(a):
        mini += 1
        a.append(scores[i])
    else:
        a.append(scores[i])

print(mini, maxi)