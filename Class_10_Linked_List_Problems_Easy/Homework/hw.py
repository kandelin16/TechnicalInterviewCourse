class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():    
    def __init__(self):
        self.head = None

    def AddNode(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
