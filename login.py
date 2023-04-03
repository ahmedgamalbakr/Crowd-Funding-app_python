from helpermodule import askforName
from projects import fundraise_project

def login():

    user_name = askforName("Enter your name : ")
    password = input("Enter your password: ")

    try:
     
     fileobj=open("users.txt", "r") 

    except Exception as e:
     return False
    
    else:
     
     for line in fileobj:
           stored_username= line.strip().split(":")[0]
           stored_password= line.strip().split(":")[4]
           if user_name == stored_username and password == stored_password:
            print("Login successful!")
            fundraise_project()
            return
       
    print("user does not exist")
