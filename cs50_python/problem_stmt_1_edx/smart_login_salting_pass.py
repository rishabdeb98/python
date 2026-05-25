import hashlib
import json
import os   
import secrets

#file to store user data
USER_FILE="user.json"

#Hashing password using SHA256
def hash_password(password,salt=None):
    if salt is None:
        salt=secrets.token_hex(16) #generate a random 16-byte salt
    hashed=hashlib.sha256((salt+password).encode()).hexdigest()
    return salt,hashed

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE,"r") as f:
            return json.load(f)
    return{}

#save user to a file
def save_user(user):
    with open(USER_FILE,"w") as f:
        json.dump(user,f)

#register new user
def register(user):
    username=input("Choose username ")
    if username in user:
        print(f"User already exists,{username}")
        return user
    password=input("Choose password ")
    hashed,salt=hash_password(password)
    user[username]={"hash":hashed,"salt":salt}#store both hash and salt
    save_user(user)
    print("Registaration successful! ")
    return user

def login(user):
    username=input("Enter username ")
    password=input("Enter password ")
    if username in user:
        stored_hash=user[username]["hash"]
        stored_salt=user[username]["salt"]
        hashed, _=hash_password(password,stored_salt)
        if hashed==stored_hash:
            print(f"Login successful! Welcome {username}")
            return
        print("Invalid username or password")
        
def main():
    user=load_users()
    while True:
        print("\nOptions: [1]Register [2]Login [3]Exit")
        choice=input("Enter choice ")
        if choice=="1":
            user=register(user)
        elif choice=="2":
            login(user)
        elif choice =="3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
