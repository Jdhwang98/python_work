rivers = {
    "tigres" : "Iraq",
    "nile" : "egypt",
    "yellow river" : "china",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThese are all the rivers' names: ")
for river in rivers.keys():
    print(f" -{river.title()}")

print("\nThese are all the countries with rivers names: ")
for country in rivers.values():
    print(f" -{country.title()}")
