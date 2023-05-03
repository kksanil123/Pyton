# f = lambda x: x + 2
# print(f(2))
#
# li = ['an may', 'zal do', 'bal highs', 'kin dead', 'joy cut', 'plane yo', 'cat line', 'a']
# li.sort()
# print(li)
# li.sort(key=lambda name: name.split(' ')[-1].lower())
# print(li)


# k = lambda a, b, c, x: a * x ** 2 + b * x + c
# print(k(2, 3, -5 ,0))


def quadratic(a, b, c,):
    return lambda x: a * x ** 2 + b * x + c


print(quadratic(2, 3, 4))
print(quadratic(2, 3, 4)(0))
f = quadratic(2, 3, 4)
print(f(0))
