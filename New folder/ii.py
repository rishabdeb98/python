camel=input("CamelCase")
snake=""

for ch in camel:
    if ch.endswith==" ":
        snake+="_"+ch.lower()
    else:
        snake+=ch
    print("snakeCase:",snake)