class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def printing_backwards(self):
        current_node = self.head
        if not current_node:
            print("The Linked List is empty")
        else:
            while current_node.next:
                current_node = current_node.next
            while current_node:
                print(current_node.data)
                current_node = current_node.prev

    def printing_frontwards(self):
        current_node = self.head
        if not current_node:
            print("The Linked List is empty")
        else:
            while current_node:
                print(current_node.data)
                current_node = current_node.next


linked_list = LinkedList()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
for i in months:
    linked_list.insert(Node(i))

linked_list.printing_frontwards()
