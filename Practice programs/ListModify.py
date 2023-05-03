a = [1, 13, 2, 3, 5, 8, 13, 1 , 3, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        pass

print(b)