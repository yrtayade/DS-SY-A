queue = [None] * 3
size = len(queue)
F = -1
R = -1

def insert(data):
    global F, R
    if F == (R+1)%size:
        print("FULL")
    else:
        if F == -1:
            F = 0
        R = (R + 1) % size
        queue[R] = data

def delete():
    global F, R
    if F == -1 :
        print("EMPTY")
    else:
        x = queue[F]
        if F==R:
            F = -1
            R = -1
        else:
            F = (F + 1)%size
        
    return x

def display():
    global F, R
    if F == -1:
        print("EMPTY")
    else:
        for i in range( F, R + 1, 1):
            print( queue[i] , end= " ")
    print()

insert('A')
insert('B')
insert('C')

display()
