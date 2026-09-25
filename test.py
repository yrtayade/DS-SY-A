stack = [None] * 5
top = -1
size = len(stack)

def push(data):
    global top
    if top == (size-1):
        print("FULL")
    else:
        top = top + 1
        stack[top] = data

def pop():
    global top
    if top == -1:
        print("Empty")
    else:
        x  = stack[top]
        top = top -1
        return x

def display():
    global top
    if top == -1:
        print("EMPTY")
    else:
        for i in range(0,top+1):
            print(stack[i], end=" ")
        print()


name = "Welcome"

print(pop())
print(pop())
print(pop())
print(pop())