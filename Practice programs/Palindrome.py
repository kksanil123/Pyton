st = input("Enter a string")
for i in range(0, (len(st)//2)):
    if st[i] == st[-i-1]:
        if i == (len(st)//2)-1:
            print("This is palindrome")
            break
        else:
            pass
    else:
        print("Not a palindrome")


