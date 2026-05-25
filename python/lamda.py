people=[
    {"Name":"Rishabh","house":"Gryffindor"},
    {"Name":"Ritvik","house":"America"},
    {"Name":"Montu","house":"Bihar"},
]

people.sort(key=lambda person:person["Name"])
print(people)

#this program makes the name or houses in alphabetical order