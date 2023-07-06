def solution(arr: [int]) -> list:
    a, b = [], []
    for item in arr:
        if arr.count(item) > 1:
            a.append(item)
            break

    for i in range(len(arr)):
        if arr[i] == a[0]:
            b.append(i + 1)

    a.append(b[-1])

    return a


print(solution(list(map(int, input().split()))))

