def solution(s: str) -> int:
    x = s.split('-')
    a = 1
    while not x[-a]:
        a += 1

    return len(x[-a])


print(solution(input()))