#structure of a node
class Node:
    info = None
    next = None

class SLLOperation:
    start = None
    def insertAtBeg(self, data):
        #creating Node with data
        newNode = Node()
        print("Address: ", newNode)
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    
    def insertAtEnd(self, data):
        #creating Node with data
        newNode = Node()
        print("Address: ", newNode)
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start = newNode
        else:
            p = self.start
            while p.next != None:
                p = p.next            
            p.next=newNode
    
    def display(self):
        if self.start ==None:
            print("Empty List")
        else:
            p = self.start
            while p!=None:
                print( p.info , end = " ")
                p = p.next

s1 = SLLOperation()
s1.insertAtBeg(20)
s1.insertAtBeg(60)
s1.insertAtBeg(80)
s1.display()
s1.insertAtEnd(66)
s1.insertAtEnd(96)
s1.display()
# output: 80  60  20 66 96  