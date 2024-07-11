# 2024-07-11 03:49:48
# 8-14. Cars: 
# Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, 
# such as a color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.


def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer" : manufacturer.title(),
        "model" : model.title(),
    }

    for info, fact in car_info.items():
        car[info] = fact
    return car

john = make_car(manufacturer="honda", model="civic", color="white", year="2019")
eryn = make_car(manufacturer="toyota", model="corola", color="black", year="2019")

print(f"\n{john}")
print(f"\n{eryn}\n")