user_input=input("Enter your age: ")

if user_input.isdigit():
    age=int(user_input)
    print("Next year you will be",age+1)
else:
    print("Invalid age")