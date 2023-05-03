import MainBefore
def fun():
    print("Printing from fun 2.")

print("Just print statement from fun2.. ")

if __name__ == "__main__":
    print("Printing this bcpz, name equals to main.. in fun2 ")
    MainBefore.fun()
else:
    print(f"Else condition exec... {__name__}")
