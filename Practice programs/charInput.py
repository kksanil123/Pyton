import datetime

name = input("Enter your name")
age = int(input("Enter your age"))
exp_year = datetime.date.today().year + (100 - age)

a = int(input("Enter how many copies.."))

print((f"Hello {name}, you will turn 100 years in the year {exp_year}" + "\n") * a)

# print(("Hi" + name +" You will turn 100 in the year" + str(exp_year)+"\n")* a)
a = int()
