age_input=input("Enter age")

if age_input.isdigit():
    age=int(age_input)
    if age>0:
        print(f"Valid age:{age}")
    else:
        print("Age must be a positive integer")
else:
    print("Invalid age only digits are allowed")

phone_input=input("Enter phone number")
if phone_input.isdigit():
    phone=int(phone_input)
    if len(phone_input)==10:
        print(f"valid phone number:{phone}")
    else:
        print("phone no. must be 10 digits long")
else:
    print(f"{phone_input} is not a valid phone no. only digits are allowed")

    
 