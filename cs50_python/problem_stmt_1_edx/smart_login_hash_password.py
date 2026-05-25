import getpass
import json
import os
import hashlib

#file to store user data
USER_FILE="users.json"

#Hashing passwords using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}
    
#Save users to file
def save_user(users):
    with open(USER_FILE,"w") as f:
        json.dump(users,f)

#Register new user
def register(users):
    username=input("choose a username")
    if username in users:
        print("User already exists")
        return users
    password=input("choose password")
    users[username]=hash_password(password)

    save_user(users)
    print("Registration Successful !")
    return users

def login(users):
    username=input("Enter username")
    password=input("Enter a password")
    users[username]=hash_password(password)

    if username in users and users[username]==hash_password(password):  
        print(f"Login successfull Welcome {username}.")
    else:
        print("Invalid Username OR Password")

def main():
    users=load_users()
    while True:
        print("\nOptions: [1]Register [2]Login [3]Exit")
        choice=input("Enter choice")

        if choice=="1":
            users=register(users)
        elif choice=="2":
            login(users)
        elif choice=="3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()