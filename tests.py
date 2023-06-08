class Node:
    def __init__(self, data=None):
        self.data = data
        self.pointer = None


class LinkedList:
    def __init__(self):
        self.item = None

    def printing(self):
        printval = self.item
        while printval is not None:
            print(printval.data)
            printval = printval.pointer



a1 = LinkedList()
a1.item = Node("Monday")
a2 = Node("Tuesday")
a3 = Node("Wednesday")

# linking a1 to a2
a1.item.pointer = a2
a2.pointer = a3

a1.printing()