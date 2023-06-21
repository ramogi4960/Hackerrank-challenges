# let's implement queues
class Node:
    def __init__(self, data):
        self.data = data
        self.down = None


class Queue:
    def __init__(self, top):
        self.top = Node(top)
        self.down = None

    def enqueue(self, data):
        if not self.top:
            self.top = Node(data)
        else:
            a = self.top
            while a.down:
                a = a.down
            a.down = Node(data)

    def dequeue(self):
        a = self.top
        self.top = self.top.down
        del a

    def print_queue(self):
        if not self.top:
            print("The queue is empty")
        else:
            a = self.top
            while a:
                print(a.data)
                a = a.down


my_queue = Queue(1)
for number in range(2, 11):
    my_queue.enqueue(number)

my_queue.dequeue()
my_queue.print_queue()

