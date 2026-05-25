while True:
    value=input("Enter a number between 1 and 10: ")
    if value.isdigit() and 1 <= int(value) <=10:
        break
    print("Invalid input. Try again.")