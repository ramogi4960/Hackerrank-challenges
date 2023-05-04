# we are given number of athletes N and number of attributes M for each athlete
# we are also given an int K which is an index of an item in the attributes M
# we are supposed to print out the list of M attributes as sort using the K index of the attributes
# we can get the attribute at K and append a new list
# after that, we can iterate through that sorted list and print the list of attributes
# that contains the iterating value of item in the K list
no_of_athletes, no_of_attributes= list(map(int, input().split()))
a = []
for i in range(no_of_athletes):
    attributes = list(map(int, input().split()))
    a.append(attributes)

K = int(input())
for i in sorted(a, key=lambda i: i[K]):
    print(*i)