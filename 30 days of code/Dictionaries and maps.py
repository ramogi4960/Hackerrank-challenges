phonebook, final = dict(tuple(input().split()) for _ in range(int(input()))), []

while True:
    try:
        final.append(input())
    except:
        break

for item in final:
    if item in phonebook.keys():
        print(f"{item}={phonebook[item]}")
    else:
        print("Not found")
