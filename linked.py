class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertend(self, ele):
        if self.head is None:
            self.head = ele
        else:
            last_node = self.head
            while True:
                if last_node is None:
                    break
                else:
                    last_node = last_node.next
            last_node.next = ele
first_ele = Node("harith")
linkedlist = Linkedlist()
