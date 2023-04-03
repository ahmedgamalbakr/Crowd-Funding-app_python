#Authentication System 
from helpermodule import *
from fileopreations import save_user_toFile

def signUP():
    
    first_name = askforName("Enter your first name: ")
    last_name = askforName("Enter your last name: ")
    email = askforEmail("Enter your email: ")
    mobile_phone = askforPhone("Enter your mobile phone number: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    
    while True:
        if password != confirm_password:
            print("Passwords do not match")
            confirm_password = input("please Enter Confirm password again: ")
        else:
            break

    user_info=f"{first_name}:{last_name}:{email}:{mobile_phone}:{password}:{confirm_password}\n"
    
    #Save user Data into File
    save_user_toFile(user_info)
    print("The user has already saved successfully.")


    