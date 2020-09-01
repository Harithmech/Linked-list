#linked list 

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
                if last_node.next is None:
                    break
                else:
                    last_node = last_node.next
            last_node.next = ele

    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next

    def length(self):
        currentnode = self.head
        count = 0
        while currentnode.next is not None:
            count += 1
            currentnode = currentnode.next
        print(count)


first_ele = Node("harith")
linkedlist = Linkedlist()
linkedlist.insertend(first_ele)
second_ele = Node("harshith")
linkedlist.insertend(second_ele)
linkedlist.printlist()
linkedlist.length()