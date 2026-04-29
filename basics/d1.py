data = {}
user_number = input("enter number of users: ") 

for i in range(int(user_number)):
    user = input(f"enter user {i}: ")
    password = input(f"enter password {i}: ")
    data[user] = {"password": password}

print("login page")
for i in range(1,4):
    name = input("enter name: ")
    pw = input("enter password: ")
    if name in data and data[name]["password"] == pw:
        print("logged in")
        print("Welcome " + name)
        break
    else:
        print("login failed")
        print(f"{3-i} attempts left")
        if i == 3:
            print("account locked")
