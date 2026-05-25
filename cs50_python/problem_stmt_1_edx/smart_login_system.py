import getpass

stored_username="ritvik123"
stored_password="1234"
user_input=input("Username").strip().lower()
password=getpass.getpass("Enter password")

if user_input==stored_username and password==stored_password:
    print("Login successful")

else:
    print("Login failed")