# first, we have n integers in an array.
# then we have arrays A and B. Each have m integers.
# if an integer in our first array exists in A, we add 1 to happiness. If it's in B, we add -1
# so we create an array and then check if each integer in the array exists in A or B.
# we then output the total happiness.
n, m = map(int, input().split())
list1 = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))
happiness = 0
for i in range(n):
    if list1[i] in A:
        happiness += 1
    if list1[i] in B:
        happiness -= 1

print(happiness)
