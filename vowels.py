x=input("Enter character: ") 
vowels="aeiou" 
output=" "  

for ch in x: 
    if ch not in vowels: 
        output+=ch
print(output)