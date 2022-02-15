class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
    def addNode(self,node):
        if self.head == None:
            self.head = node
        else:
            tempnode = self.head
            while (tempnode.next != None):
                tempnode = tempnode.next
            tempnode.next = node
    def getHead(self):
        return self.head
    
    def reverse(self):
        nodeArray = []
        returnableList = List()
        node = self.getHead()
        while node.next != None:
            nodeArray.append(node)
            node = node.next
        nodeArray.append(node)
        
        for index in range(len(nodeArray)-1, -1, -1):
            nodeArray[index].next = None
            returnableList.addNode(nodeArray[index])
        return returnableList

    def reverseFast(self):
        previousNode = None
        currentNode = self.getHead()
        while (currentNode is not None):
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode
        return self
    
    def printLL(self):
        node = self.getHead()

        while node.next != None:
            print(node.data)
            node = node.next
        print(node.data)

    def removeNode(self,data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != None:
                if current.next.data == data:
                    current.next = current.next.next
                else:
                    current = current.next
    

node1 = Node("first data")
node2 = Node("second data")
node3 = Node("third data")
linkedList = List()

linkedList.addNode(node1)
linkedList.addNode(node2)
linkedList.addNode(node3)

reversedList = linkedList.reverseFast()
#reversedList.printLL()


# reverse a linked list
reversedList.removeNode("second data")
reversedList.printLL()
