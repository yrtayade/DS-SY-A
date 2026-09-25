class Node:
    info = None
    next = None

class Operation:
    start = None
    def insertAtBeg(self, data):
        newNode = Node()
        newNode.info = data
        newNode.next = None

        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode

    def insertAtMid(self, data, pos):
        newNode = Node()
        newNode.info = data
        newNode.next = None
        if self.start == None:
            self.start = newNode
        else:
            p = self.start
            while p.info != pos:
                p = p.next
            q = p.next
            p.next = newNode
            newNode.next = q

    def insertAtend(self, data):
        newNode = Node()
        newNode.info = data
        newNode.next = None
        if self.start == None:
            self.start = newNode
        else:
            p = self.start
            while p.next!=None:
                p = p.next
            p.next= newNode

    def display(self):
        if self.start == None:
            print("Empty List")
        else:
            p = self.start
            while p!=None:
                print(p.info , end = " ")
                p = p.next
        print()

s1 = Operation()
s1.insertAtBeg(22)
s1.insertAtBeg(62)
s1.insertAtBeg(92)
s1.insertAtBeg(88)
s1.display()
s1.insertAtMid(55, 62)
s1.display()
s1.insertAtend(30)
s1.display()

s2 = Operation()
s2.insertAtBeg(99)
s2.insertAtend(11)
s2.insertAtend(33)
s2.display()

# logic for merging two list
temp = s1.start
while temp.next!=None:
    temp = temp.next
temp.next = s2.start

s1.display()