a = [
    {"name": "Kevin",
     "age": 31},
    {"name": "Alice",
     "age": 30}
]
# result = dict(sub.values() for sub in a)
# print(result)
# for i in a:
#     print(i.values())

for i in a:
    print(dict(i.values()))