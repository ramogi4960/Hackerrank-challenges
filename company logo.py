from collections import Counter
for a in Counter(sorted(input())).most_common(3):
    print(*a)

