pets = []

pet = {
    "name" : "max",
    "breed" : "mixed",
    "owner" : "john",
}

pets.append(pet)

pet = {
    "name" : "dobie",
    "breed" : "dobberman",
    "owner" : "eryn",
}

pets.append(pet)

pet = {
    "name" : "fyn",
    "breed" : "mixed",
    "owner" : "kyle",
}

pets.append(pet)

pet = {
    "name" : "pooka",
    "breed" : "mixed",
    "owner" : "carlos",
}

pets.append(pet)

pet = {
    "name" : "gold",
    "breed" : "goldfish",
    "owner" : "jaxson",
}

pets.append(pet)

pet = {
    "name" : "gong hey",
    "breed" : "black",
    "owner" : "crystal",
}

pets.append(pet)

pet = {
    "name" : "funny",
    "breed" : "chihuahua",
    "owner" : "josiah",
}

pets.append(pet)

for pet in pets:
    name = f"{pet["name"].title()}"
    breed = f"{pet["breed"].title()}"
    owner = f"{pet["owner"].title()}"
    print(f"{name} is a {breed} owned by: {owner}")
