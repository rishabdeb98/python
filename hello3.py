#Ask user for name
n=input("What is your name").strip().title()#Remove white space from str and capitalize it
#say hello to user
first,last=n.split(" ")
print(f"Hello,{first}")                