import sys
"""
Test cases
6
3
5
4
7
2
1
"""

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        if not root:
            pass
        else:
            l = [root, ]
            final = [root.data, ]
            while l:
                a = l.pop(0)
                if a.left:
                    l.append(a.left)
                    final.append(a.left.data)
                if a.right:
                    l.append(a.right)
                    final.append(a.right.data)
            print(*final, sep=" ")

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)