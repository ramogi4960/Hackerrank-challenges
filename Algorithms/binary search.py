import datetime


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left+right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
            return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


def binary_search(array, target) -> bool:
    a = sorted(array)
    while len(a) != 1:
        if a[len(a)//2] == target:
            return True
        elif a[len(a)//2] > target:
            a = a[:len(a)//2]
        elif a[len(a)//2] < target:
            a = a[len(a)//2:]
    # [1, 2, 3, 4, 5]
    if a[0] == target:
        return True
    else:
        return False

