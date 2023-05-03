num = int(input("Enter a number"))

if num%2 ==0:
    if (num/2)%2 == 0:
        print("You entered a number which is a multiple 4")
    else:
        print("You entered an even number")
else:
    print("You entered an odd number")

