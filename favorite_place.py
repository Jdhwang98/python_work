favorite_places = {
    "john" : ["home", "getti museum", "huntington library"],
    "eryn" : ["garfield park", "santa monica bluffs", "thailand"],
    "carlos" : ["home", "grandparents house", "wingstop"],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are: ")
    for place in places:
        print(f"{place.title()}")