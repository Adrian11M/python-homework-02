USERNAME = "student"
PASSWORD = "python123"

attempts=0
while attempts<3:
    my_username=input("Username: ")
    my_password=input("Password: ")

    if my_username.lower() == USERNAME and my_password == PASSWORD:
        print("welcome")
        break

    else:
        attempts=attempts+1
        attempts_left=3-attempts
        if attempts_left>0:
            print(f"Wrong credentials,{attempts_left} attempts left ")
        else:
            print("Account locked")
