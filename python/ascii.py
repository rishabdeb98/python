x=input("Enter a character: ")
count=0
for ch in x:
    if ch.isupper():
        count=count+1
print("Number of uppercase characters: ",count)