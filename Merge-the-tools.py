def merge_the_tools(string, k):
    t = []
    U = []
    for K in range(0, len(string), k):
        t.append(string[K: k + K])
        # print(t)
    for i in range(0, len(t)):
        u = []
        temp = t[i]
        temp.split()
        u.append(temp[0])
        for j in temp[1: len(temp)]:
            if j in str(u):
                pass
            else:
                u.append(j)
        u = "".join(u)
        U.append(u)

    U = "\n".join(U)
    print(U)


