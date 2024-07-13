# 2024-07-12 02:41:35
# 9-4. Number Served: 
# Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}")
        print(f"They serve: {self.cuisine_type} food")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for bussiness!\n")
        
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served
        
person_one = Restaurant("mcDonalds", "american")
person_one.open_restaurant()
person_one.set_number_served(100)
print(f"{person_one.number_served} people served")
person_one.set_number_served(200)
print(f"{person_one.number_served} people served")
person_one.increment_number_served(55)
print(f"{person_one.number_served} people served")
    