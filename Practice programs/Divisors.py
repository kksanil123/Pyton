num = int(input("Enter a number"))

print([i for i in range(2,num//2+1) if num%i ==0])