def save_user_toFile(user_info):
    try:
        fileobj=open('users.txt','a')
    except Exception as e:
        return False
    else:
        fileobj.write(user_info)
        return True



