
class Student:
    def getData(self):        
        self.roll = int(input("Enter Roll: "))
        self.name = input("Enter Name: ")
        self.per = float(input("Enter Per: "))
        print() 

    def display(self):
        print(self.roll, self.name, self.per)

# array of objects
s = [None] * 4
for i in range( len(s)):
    s[i] = Student()

for i in range(len(s)):
    s[i].getData()

for i in range(len(s)):
    s[i].display()

print("Topper: ")
max = 0
for i in range(len(s)):
    if max < s[i].per:
        max = s[i].per 
        pos = i

s[pos].display()