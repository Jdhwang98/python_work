# 2024-07-11 20:33:08
# 9-1. Restaurant: 
# Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        
    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}")
        print(f"They serve: {self.cuisine_type} food")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for bussiness!\n")

# case 1
place_one = Restaurant("road to seoul", "asian")
print(place_one.restaurant_name)
print(place_one.cuisine_type)
place_one.describe_restaurant()
place_one.open_restaurant()

# case 2
place_two = Restaurant("skaff's", "lebonese")
place_two.describe_restaurant()
place_two.open_restaurant()

# case 3 
place_three = Restaurant("the hat", "american fast food")
place_three.describe_restaurant()
place_three.open_restaurant()
