def add(x, y):
    print(x+y)

def sub(x, y):
    print(x-y)

while True:
    choice = int(input("Enter 1. Add 2. sub 0.Exit : "))
    if choice<0 or choice>2:
        print("Invalid")
    else:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))        
        if choice ==1:
            add(num1, num2)
        if choice ==2:
            sub(num1, num2)
        if choice == 0:
            break
    
