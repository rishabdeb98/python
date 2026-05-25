def func1(name):
    return f"Hello,{name}! Welcome"
if __name__=="__main__":       #run the following code only if this file is being executed directly, not when it’s imported.
    user_name=input("Enter your name:")
    print(func1(user_name))