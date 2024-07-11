# 7-10. Dream Vacation: 
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

name_prompt = "Please enter your name: "
place_prompt = "Please enter the place you would like to visit: "
continue_prompt = "Please enter 'yes' to continue or 'no' to end program: "

places = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    places[name] = place

    repeat = input(continue_prompt)
    if repeat != "yes":
        break

for name, place in places.items():
    print(f"{name.title()} want's to go to {place.title()}")