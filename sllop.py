class Node:
    info = None
    next = None

class Operation:
    start = None
    temp = None
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

    def delete(self, data):
        if self.start == None:
            print("Empty List")
        else:            
            temp = self.start
            while temp.info != data:
                p = temp
                temp = temp.next
            
                if temp == None:
                    print("NO data found")    
                    return
            
            if temp == self. start:
                self.start = temp.next
                temp.next = None
                temp = None
            elif temp.next == None:
                p.next = None
                temp = None
            else:
                q = temp.next
                p.next = q
                temp = None
    



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
s1.insertAtMid(55, 62)
s1.insertAtend(30)
s1.display()
s1.delete(55)
s1.display()
s1.delete(88)
s1.display()
s1.delete(30)
s1.display()
s1.delete(1)
s1.display()