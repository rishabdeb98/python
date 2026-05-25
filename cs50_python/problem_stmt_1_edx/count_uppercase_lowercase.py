text=input("Enter some text: ")
upper=lower=digit=special=0
special_chars=[]
for ch in text:
    if ch.isupper():
        upper+=1
       
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1 
        special_chars.append(ch)  

print("Upper case",upper)
print("Lower case",lower)
print("Digits",digit)
print("Special character",special,"-->",special_chars)