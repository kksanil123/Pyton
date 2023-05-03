# try:
#    raise NameError('HiThere')
# except NameError as e:
#     print('An exception flew by!', e)
#     raise

def divide(x, y):
   try:
        result = x / y
   # except BaseException:
   #     print('Handled through Base exception')
   # except ZeroDivisionError:
   #     print("division by zero!")
   # else:
   #      print("result is", result)
   finally:
       print("executing finally clause")

divide(2, 0)