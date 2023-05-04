A, number_of_subsets, b = set(map(int, input().split())), int(input()), True
for i in range(number_of_subsets):
    p = set(map(int, input().split()))
    if not p.issubset(A):
        b = False
print(b)