num = int(input("Enter how many digits you want to print in fibonacci series"))
a,b =0,1
count = 0
fib =[]
if(num<3 and num>0):
    print(a,b)
elif(num>=3):
    fib.append(a)
    fib.append(b)
    count = 2
    while(count<num):
        c = a+b
        fib.append(c)
        a=b
        b=c
        count = count + 1
    print(fib)
else:
    print("Something went wrong, Please try again with a number > 2")



