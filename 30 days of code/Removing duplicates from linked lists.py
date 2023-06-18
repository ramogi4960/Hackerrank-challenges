"""
test case
6
1
2
2
3
3
4

20
3
9
9
11
11
11
11
89
89
100
100
101
102
103
108
200
250
250
250
250
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        l, current = set(), head
        while current:
            l.add(current.data)
            current = current.next
        c = None
        for i in sorted(list(l)):
            c = self.insert(c, i)
        return c

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
