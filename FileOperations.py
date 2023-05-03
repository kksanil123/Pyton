# with open("test1.txt", 'r') as f1:
#     print(f1.read())

# with open("Test2.txt",'w') as f2:
#     for i in range(11):
#         f2.write(str(i))
#         f2.write('\n')

# with open("Test2.txt",'r+') as f3:
#     for line in f3:
#         print(line)


# with open("Test2.txt",'r+') as f3:
#     for i in f3:
#         print(f3.readline())
#         print("-------")
import json

d= {"id":37,"category":{"id":0,"name":"Testing_pet_37"}}
print(str(d))
print(dict(d))

with open("Test1.txt",'r') as f5:
    k= f5.read()
    print(k)
    print(type(k))
    k1=json.loads(k)
    print(k1)
    print(type(k1))




# with open("Test2.txt", 'r+') as f4:
#   while f4.readline():
#     print(f4.tell()) #returns the location of the next line