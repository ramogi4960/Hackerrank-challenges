from typing import List


def solution(s: str) -> int:
    final_list = []
    for i in range(1, len(s)):
        x, y = s[:i], s[i:]
        final_list.append(x.count('x') + y.count('o'))

    return max(final_list)


if __name__ == '__main__':
    a = input()
    output = solution(a)
    print(output)