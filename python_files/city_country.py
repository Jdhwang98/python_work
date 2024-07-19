# 8-6. City Names: 
# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city,country):
    return (f"{city.title()}, {country.title()}")

city = city_country("taipei" ,"taiwan")
print(city)

city = city_country("seoul" ,"south korea")
print(city)

city = city_country("los angeles" ,"united states")
print(city)