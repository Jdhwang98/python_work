cities = {
    "los angeles" : {
        "state" : "california",
        "country" : "united states",
        "population" : 3_000_000
    },
    "new york city" : {
        "state" : "new york",
        "country" : "united states",
        "population" : 8_000_000
    },
    "dallas" : {
        "state" : "texas",
        "country" : "united states",
        "population" : 1_000_000
    }
}

for city, facts in cities.items():
    state = facts["state"].title()
    country = facts["country"].title()
    population = facts["population"]
    
    print(f"{city.title()} is in {country}, {state}")
    print(f" It's population size is: {population}\n")
   
    
   