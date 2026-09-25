#Find the given number is present in list or not num = 8 -> Found num=7 ->Not Found
x = [4, 6, 9, 8, 3]
num = 88
check = 0
for i in range(x):
    if i == num:        
        check = 1
        break    

if check == 1:
    print("Found")
else:
    print("Not Found")