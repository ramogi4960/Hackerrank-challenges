# the substring has to be preceeded by or followed by a \w
import re
sentences = [input() for _ in range(int(input()))]
sub_words = [input() for _ in range(int(input()))]
for item in sub_words:
    pattern = rf"(?<=\w){item}(?=\w)"
    count = 0
    for i in sentences:
        if re.search(pattern, i):
            count += len(re.findall(pattern, i))
    print(count)
