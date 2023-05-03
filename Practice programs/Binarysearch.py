l = [70, 2]


# no = int(input("Enter a number between 1 and 500 to search whether it is present in the list."))


def bs_tree(a, b):
    print(a, len(a))
    if len(a) > 0:
        if b == a[len(a) // 2]:
            print("Number found.")
        elif b > a[len(a) // 2]:
            bs_tree(a[(len(a) // 2):], b)
        else:
            bs_tree(a[:(len(a) // 2)], b)
    else:
        print("Number not found...")


bs_tree(l, 70)
