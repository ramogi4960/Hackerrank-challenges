# let's try to implement bst ourselves
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BNS:
    def insert(self, root, data):
        if not root:
            root = Node(data)
        else:
            if data <= root.data:
                l = self.insert()
