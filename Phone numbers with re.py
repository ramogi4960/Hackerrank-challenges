import re
numbers_list = []
for i in range(int(input())):
    numbers_list.append(input())
for item in numbers_list:
    print("YES" if re.search(r"^[789][0-9]{9}$", item) is not None else "NO")