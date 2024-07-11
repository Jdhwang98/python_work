people = []

person = {
    "first_name" : "johnathan",
    "last_name" : "hwang",
    "age" : 25,
    "city" : "alhambra",
}

people.append(person)

person = {
    "first_name" : "eryn",
    "last_name" : "bollin",
    "age" : 30,
    "city" : "south pasadena",
}

people.append(person)

person = {
    "first_name" : "fred",
    "last_name" : "Hwang",
    "age" : 47,
    "city" : "Alhambra",
}

people.append(person)

for person in people:
    full_name = f"{person["first_name"].title()} {person["last_name"].title()}"
    age = f"{person["age"]}"
    city = f"{person["city"].title()}"
    print(f"{full_name} of {city} is {age} years old.")