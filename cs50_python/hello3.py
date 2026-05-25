#Ask user for namespace from str 
n=input("What is your name").strip().title()#Remove white and capitalize it
#say hello to user
first,last=n.split(" ")
print(f"Hello,{last}")                  