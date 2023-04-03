import re

#function to validate name 
def askforName(message):
    while True:
        name = input(message)
        if name.isalpha():
            return name
        print("--- invalid name please enter it again ---")


#function to validate num 
def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("--- invalid number please enter it again ---")


#function to vlaidate email
def askforEmail(message):
    while True:
        email = input(message)
        pattern = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
        if re.match(pattern, email):
            return  email
        print("--- invalid email please enter it again ---")


#function to validate egy-phone
def askforPhone(message):
    while True:
        phone = input(message)
        pattern = r'^[0-9]{3}-[0-9]{3}-[0-9]{5}$'
        if re.match(pattern, phone):
            return  phone
        print("--- invalid phone please enter it again ---")



