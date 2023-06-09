months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November"]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def insert_tail(self, new_node):
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def printing(self):
        if not self.head:
            print("The linked list is empty")
        else:
            current_node = self.head
            while True:
                print(current_node.data)
                current_node = current_node.next
                if current_node == self.head:
                    break


linked_list = Linked()
for item in months:
    linked_list.insert_tail(Node(item))

linked_list.printing()
