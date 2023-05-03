import random
import string

print("Welcome to the Cows and Bulls game.")

guess_count = 0

while(True):
    cows = 0
    bulls = 0
    sys_no = random.choices(string.digits, k=4)
    print(sys_no)
    usr_no = input("Enter the guessed 4 digit number....")

    for i,j in enumerate(sys_no):
                if j == usr_no[i]:
                    cows = cows+1
                    pass
                else:
                    bulls = bulls + 1
                    pass

    guess_count = guess_count + 1

    if cows == 4:
        print(f"You guessed correct after {guess_count-1} tries. ")
        break
    else:
        print(f"Cows = {cows}, Bulls = {bulls}")
        print("Please try again....")
        pass



