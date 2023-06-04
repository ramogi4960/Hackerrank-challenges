import re
"""
10
businessman video demeanor demeanor dishonest acknowledge dvd honor sister opportunity
keen labour artistic favourite red definition impatient take behaviour warmth
favourite december associated legal examine performance construction savoury prior infected
explanation establish unfriendly speed pointed slip candy one behaviour honor
woman lot basic throw honor somebody pollution use dog unhappiness
disgust attract penny reduction performance teacher ally splendor smash pilot
kindness labour aged demeanor remains cough immoral request rancor lesson
soap behavior vision happen new disc generously favorite l melt
mathematics candidate none keen honour lift jam savoury large dr
accept restriction young library similar film confront direct stone honour
7
behaviour
honour
demeanour
splendour
savoury
favourite
rancour
"""
N_list, T_list = [input() for _ in range(int(input()))], [input() for _ in range(int(input()))]
for item in T_list:
    count = 0
    if re.search(r"our", item):
        a = re.sub(r"our", "or", item)
        for i in N_list:
            if re.search(rf"\b({a}|{item})\b", i):
                count += len(list(re.findall(rf"\b({a}|{item})\b", i)))
    elif re.search(r"or", item):
        a = re.sub(r"or", "our", item)
        for i in N_list:
            if re.search(rf"\b({a}|{item})\b", i):
                count += len(list(re.findall(rf"\b({a}|{item})\b", i)))
    else:
        pass
    print(count)