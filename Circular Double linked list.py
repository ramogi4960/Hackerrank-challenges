class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, new_node):
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def insert_head(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
            a = self.head
            self.head = new_node
            self.head.next = a
            self.head.prev = current_node
            del a

    def printing(self):
        if not self.head:
            print("The Linked list is empty")
        else:
            current_node = self.head
            while current_node.next is not self.head:
                print(current_node.data)
                current_node = current_node.next
            print(current_node.data)


linked_list = LinkedList()
linked_list.insert_tail(Node("February"))
linked_list.insert_tail(Node("March"))
linked_list.insert_head(Node("January"))
linked_list.printing()
