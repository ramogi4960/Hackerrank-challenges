# in this task, we are supposed to implement the bubble sort
# we need to compare each element with the next one and swap them if the element is greater than the next.
# this is done until the list is sorted, or rather, when there are no more swaps
# we can do this by first starting a loop that continues so long as the list is not sorted
# next, we need to start a loop that checks if the current element is greater than the next

def bubble_sort(a: list, n: int):
    swaps = 0
    for i in range(n):
        x = a[0]
        for number in range(1, n):
            if x > a[number]:
                a[number - 1] = a[number]
                a[number] = x
                swaps += 1
            else:
                x = a[number]
