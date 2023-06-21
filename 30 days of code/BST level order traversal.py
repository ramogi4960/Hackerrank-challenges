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
        final = []
        if not root:
            print("The BST is empty")
        else:
            a, l = [root, ], []
            while a:
                for item in a:
                    final.append(item)
                    if item.left:
                        l.append(item.left)
                    if item.right:
                        l.append(item.right)
                a = [item for item in l]
                l.clear()

        for item in final:
            print(item.data, end=" ")


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
