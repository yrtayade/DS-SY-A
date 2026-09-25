stack = []
exp = input("Enter postfix expression with space: ")
newExp = exp.split(" ")
for i in newExp:
    if i.isdigit():
        stack.append( int(i) )
    else:
        num2 = stack.pop()
        num1 = stack.pop()       
        if i == '*':
            result =num1 * num2
            stack.append( result )
        elif i == '/' :
            result =num1 / num2
            stack.append( result )
        elif i == '+' :
            result =num1 + num2
            stack.append( result )
        elif i == '-' :
            result =num1 - num2
            stack.append( result )
print( stack.pop()  )
