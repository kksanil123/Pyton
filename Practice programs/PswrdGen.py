import random
import string

A = string.ascii_lowercase
B = string.ascii_uppercase
C = string.ascii_letters
D = string.digits
E = string.punctuation


def pswd_gen(a, *b):
    base_pswd = ''.join(random.choices(a, k=8))
    for i in b:
        base_pswd = base_pswd.join(random.choices(i, k=2))
    else:
        final_pswd = base_pswd

    return final_pswd


pswd_ch = int(input("Please choose a number from below to generate a password..\n\
                1.Strong password \n\
                2.Weak password\n\
                3.Very weak password"))

match (pswd_ch):
    case 1:
        print(pswd_gen(C, D, E))
    case 2:
        print(pswd_gen(C, D))
    case 3:
        print(pswd_gen(C))
    case _:
        print("Invalid choice")
