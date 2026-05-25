import getpass

users={
    "ritvik@123": "montumoni",
    "rishabh@33":"tunit123",
    "babulal90":"xtrt22"
}
username=input("username ").lower()
password=getpass.getpass("Enter password")

if username==users and users[username]==password:
    print(f" Login successfull!,{username}")

else:
    print("Invalid username or password")
