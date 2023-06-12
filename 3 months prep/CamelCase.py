def camel_case(a:list) -> str:
    final = ""
    if a[0] == "S":
        if a[1] == "M":
            word = a[2][:-2]
            for i in word:
                if i.isupper():
                    b = i.lower()
                    final += f" {b}"
                else:
                    final += i
        elif a[1] == "V":
            word = a[2]
            for i in word:
                if i.isupper():
                    b = i.lower()
                    final += f" {b}"
                else:
                    final += i
        else:
            word = a[2][1:]
            final += a[2][0].islower()
            for i in word:
                if i.isupper():
                    b = i.lower()
                    final += f" {b}"
                else:
                    final += i
    else:
        if a[1] == "V":
            word = a[2].split()
            final += word[0]
            for i in range(1, len(word)):
                final += word[i].capitalize()
        elif a[1] == "C":
            for item in a[2].split():
                final += item.capitalize()
        else:
            word = a[2].split()
            final += word[0]
            for i in range(1, len(word)):
                final += word[i].capitalize()
            final += "()"
    return final


print(camel_case(input().split(";")))
