import operator as op

people = [input().split() for i in range(int(input()))]
print(sorted(people, key=op.itemgetter(2)))