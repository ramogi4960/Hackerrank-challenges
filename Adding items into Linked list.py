class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data: str):  # the new_data parameter takes only strings
        new_node = Node(new_data)  # we first create a node from the arg that will be given when using the function
        if not self.head:  # we check if the linked list is empty, by checking if the head is None
            self.head = new_node  # the new node becomes the head if the linked list is empty
        else:
            n = self.head
            while n.next:  # we check if n has a next value
                n = n.next  # we iterate until n has no next value
            n.next = new_node  # if n has no next value, the iteration stops and n.next becomes the new node

    def insert_head(self, new_data: str):
        new_node = Node(new_data)
        if not self.head:  # first we check if the linked list is empty
            self.head = new_node
        else:
            a = self.head  # we create a variable to store the head value
            new_node.next = a  # we make the head value to be the next of the new node
            self.head = new_node  # we make the new node to be the head value

    def insert_somewhere(self, new_data: str, after: str):
        current_node, new_node = self.head, Node(new_data)
        while current_node: # we start an iteration to traverse through the linked list
            if current_node.data == after: # we check if after matches the point after which we want to insert
                a = current_node.next  # we create a variable for the next of that point
                current_node.next = new_node  # we make the bew bode the next of the point we chose
                new_node.next = a
                break
            else:
                current_node = current_node.next

    def printing(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.insert("Mon")
linked_list.insert("Tue")
linked_list.insert_head("Sun")
linked_list.insert("Thu")
linked_list.insert_somewhere("Wed", "Tue")
linked_list.printing()
