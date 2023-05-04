# first we create sets for each integers entered
# then we find the symmetric differences and print them vertically
N, N_set = int(input()), set(map(int, input().split()))
M, M_set = int(input()), set(map(int, input().split()))
for i in sorted(N_set.difference(M_set).union(M_set.difference(N_set))):
    print(i)