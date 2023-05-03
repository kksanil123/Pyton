# a = 2
# def f(b=a):
#     print(b)
#
# a = 5
# f()



# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(3))


def f(a, L= None):
    L=[]
    L.append(a)
    return L

print(f(1))
print(f(3))