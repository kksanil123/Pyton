print("Enter the numbers to be taken into a list.")
a = []
while(True):
    num = int(input("Enter:"))
    a.append(num)
    ch = input("Do you want to continue? Y/N")
    if ch.upper() == 'Y':
        pass
    else:
        break

def new_list(b):
    c = []
    print(b)
    if len(b) > 1:
        c.append(b[0])
        c.append(b[-1])
    else:
        print("Enter at least 2 values into the list and try again ")

    print("New list",c)

new_list(a)

