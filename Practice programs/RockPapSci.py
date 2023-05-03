import random

user_choice = input("We are playing Rock Paper Scissor game. Please enter your choice from the values [R,P,S]")

R = 0
P = 0
S = 0

match user_choice:
    case 'R':
        u_choice = 0
        P = 1
        S = -1
    case 'P':
        u_choice = 0
        S = 1
        R = -1
    case 'S':
        u_choice = 0
        R = 1
        P = -1

sys_choice = random.choice([R, P, S])

if not u_choice == sys_choice:
    print("Tie.... You chose exactly as system.")
elif u_choice > sys_choice:
    print("User won")
else:
    print("System choose", sys_choice)
    print("System won")

