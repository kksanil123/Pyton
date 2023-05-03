import random

counter = 0

while True:

    u1 = int(input("Enter a number between 0 and 10"))
    s1 = random.randint(1, 9)
    counter = counter + 1
    #print(f"system chose {s1}")
    if u1 == s1:
        print("You guessed it correct.")
    elif u1 < s1:
        print("You guessed too low.")
    else:
        print("You guessed too high.")

    ch = input("Do you want to continue(Y) or exit(N).")

    if ch.upper() == 'Y':
        pass
    else:
        print(f"you guessed correct number after {counter+1} tries.")
        break

