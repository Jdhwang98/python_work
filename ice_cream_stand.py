# 2024-07-12 11:12:38

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        
    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}")
        print(f"They serve: {self.cuisine_type} food")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for bussiness!\n")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def show_flavors(self):
        print("this is the following flavors we have: ")
        for flavor in self.flavors:
            print(flavor)

shop = IceCreamStand("coldstone")
shop.flavors = ["chocolate", "vanilla", "strawberry"]
shop.describe_restaurant()
shop.show_flavors()