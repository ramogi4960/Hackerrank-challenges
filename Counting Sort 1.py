# first we need to sort the numbers.
# then we can append the count of the iteration value
n = int(input())
arr = list(map(int, input().split()))
lexico = sorted(arr)
new_list = []

for i in range(n):
    x = lexico.count(i)
    new_list.append(x)

for i in new_list:
    print(i, end=" ")
