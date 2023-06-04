
def hourglass(array):
    ans = []
    for i in range(4):
        for x in range(4):
            a, b, c = sum(array[i][x:x+3]), sum(array[i+2][x:x+3]), array[i+1][x+1]
            count = sum([a, b, c])
            ans.append(count)

    return max(ans)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

print(hourglass(arr))
