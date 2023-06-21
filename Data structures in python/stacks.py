# let us implement Stacks
class Node:
    def __init__(self, data):
        self.data = data
        self.down = None


class Stack:
    def __init__(self, top):
        self.top = Node(top)

    def insert(self, data):
        a = self.top
        self.top = Node(data)
        self.top.down = a

    def print_stack(self):
        if not self.top:
            print("The stack is empty")
        else:
            a = self.top
            while a:
                print(a.data)
                a = a.down

    def remove(self):
        self.top = self.top.down

    def get_height(self):
        height = 0
        if not self.top:
            return height
        else:
            a = self.top
            while a.down:
                a = a.down
                height += 1
            return height


my_stack = Stack(1)
for i in range(2, 11):
    my_stack.insert(i)

my_stack.remove()
print(my_stack.get_height())
