a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Enter a number"))
for i in a:
    if i<num:
        b.append(i)

print(b)
print([x for x in a if x<5])