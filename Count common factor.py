a, b = map(int, input().split())
n, count_list = b if b >= a else a, []
for i in range(1, n+1):
    if a%i == 0 and b%i == 0:
        count_list.append(i)
print(len(count_list))