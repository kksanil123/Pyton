num = int(input("Enter a number to print fibonacci series of n numbers.."))


def fib(num):
    a, b = 0, 1
    d = [a, b]
    for i in range(2, num):
        c = a + b
        d.append(c)
        a = b
        b = c
    print(d)


fib(num)



