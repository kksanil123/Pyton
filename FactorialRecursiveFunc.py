def fibonacci(num, res = 1):
        if num in [0,1]:
            return res
        elif num > 1:
            res = res* num * fibonacci(num-1)
        else:
            return "Invalid input"

        return res

print(fibonacci(9))

