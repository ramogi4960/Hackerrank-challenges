# let's implement binary search trees in the simplest of ways

"""
Test cases
7
3
5
2
1
4
6
7
"""


# steps
# first create a Node class with left and right as none
# then create a binary search tree (BNS) class to handle the BNS. In it, we can create a function for inserting data
# the function should check if the value at a node is less than or more than the value being added
# after comparison, we compare to the left or right of that node until a point where the comparison is with a None

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    def insert(self, root, value):
        if not root:
            root = Node(value)
            return root
        else:
            current = root
            while True:
                if value < current.data:
                    if not current.left:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(value)
                        break
                    current = current.right
            return root

    def print_bst(self, root):
        final = []
        if not root:
            print("The BST is empty")
        else:
            a, l = [root, ], []
            while a:
                for item in a:
                    final.append(item)
                for item in a:
                    if item.left:
                        l.append(item.left)
                    if item.right:
                        l.append(item.right)
                a = [item for item in l]
                l.clear()

        for item in final:
            print(item.data, end=" ")

    def get_height(self, root):
        height = 0
        if not root:
            return height
        else:
            a, l = [root, ], []
            while a:
                for item in a:
                    if item.left:
                        l.append(item.left)
                    if item.right:
                        l.append(item.right)
                a = [item for item in l]
                l.clear()
                height += 1
            return height - 1


my_bst = BST()
root = None
for _ in range(int(input())):
    root = my_bst.insert(root, int(input()))

my_bst.print_bst(root)
print(my_bst.get_height(root))
