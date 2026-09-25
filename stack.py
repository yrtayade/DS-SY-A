stack = [None] * 3
top = -1
size = len( stack )

def push(data):
    global top
    if top ==(size-1):
        print("Full")
    else:
        top = top + 1
        stack[top] = data

def pop():
    global top
    if top == -1:
        print("Empty")
    else:
        x = stack[top]
        top = top - 1 

def display():
    global top
    if top == -1:
        print("Empty")
    else:
        for i in range(0, top+1):
            print( stack[i] , end = " ")
        print()

push(33)
push(55)
push(54)
push(52)
display()