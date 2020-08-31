""" #create nodes
#create linked list
#add nodes to linked list
#print linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            #self.head.next = newnode
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newnode
    def printlist(self):
        if self.head is None:
            print("list is empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next

first_node = Node("harith")
linkedlist = LinkedList()
#linkedlist.insert(first_node)
second_node = Node("pintu")
#linkedlist.insert(second_node)
third_node = Node("mathew")
#linkedlist.insert(third_node)
linkedlist.printlist() """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertend(self, ele):
        if self.head is None:
            self.head = ele
        else:
            lastele = self.head
            while True:
                if lastele.next is None:
                    break
                lastele = lastele.next
            lastele.next = ele

    def insertnode(self, ele):
        temp = self.head
        self.head = ele
        ele.next = temp
        del temp

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
        while currentnode is not None:
            currentnode = currentnode.next
            count += 1
        return count


    def insertat(self, ele, index):
        currentnode = self.head
        currentposition = 0
        while True:
            if currentposition == index:
                previousnode.next = ele
                ele.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentposition += 1

    def deletelastnode(self):
        currentnode = self.head
        while True:
            if currentnode.next is None:
                break
            previousnode = currentnode
            currentnode = currentnode.next
        previousnode.next = None
        del currentnode
linkedlist = LinkedList()
first_ele = Node("harith")
linkedlist.insertend(first_ele)
second_ele = Node("shubha")
linkedlist.insertend(second_ele)
third_node = Node("-----")
linkedlist.insertnode(third_node)
fourth_node = Node("........")
linkedlist.insertat(fourth_node, 1)
linkedlist.deletelastnode()
linkedlist.printlist()
#print(linkedlist.length())