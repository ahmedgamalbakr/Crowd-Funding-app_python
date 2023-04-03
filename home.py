from signup import signUP
from login import login

def mainMenu():
    choice= input("Please Enter S for Signup or L to login : ")
    if choice=='S':
        signUP()

    elif choice=='L':
        login()

    else:
        print("Wrong choice")

mainMenu()
