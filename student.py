class Student:
    def getData(self):        
        self.roll = int(input("Enter Roll: "))
        self.name = input("Enter Name: ")
        self.per = float(input("Enter Per: "))
        print() 

    def display(self):
        print(self.roll, self.name, self.per)

    

#creating objects
s1 = Student()
s2 = Student()
s3 = Student()

#calling getData to accept students data
s1.getData()
s2.getData()
s3.getData()

s1.display()
s2.display()
s3.display()

print("Topper: ")
if s1.per > s2.per and s1.per >s3.per:
    s1.display()
elif s2.per > s1.per and s2.per > s3.per:
    s2.display()
else:
    s3.display()