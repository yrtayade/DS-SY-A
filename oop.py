
class Student:
    roll = 0
    name = ""
    per = 0.0

    def getData(self, roll, name, per):
        self.roll = roll
        self.name = name
        self.per = per

    def display(self):
        print(self.roll, self.name, self.per)

s1 = Student()
s2 = Student()
s3 = Student()

s1.getData(101, "Mahesh", 88.8)
s2.getData(102, "Rupesh", 98.8)
s3.getData(103, "Ramesh", 68.8)
s1.display()
s2.display()
s3.display()

