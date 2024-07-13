# 2024-07-12 02:54:28
# 9-5. Login Attempts: 
# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.zip_code = zip_code
        self.login_attempts = 0
        
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f" -Name is: {full_name}")
        print(f" -Age is: {self.age}")
        print(f" -Area code is: {self.zip_code}\n")
        
    def greet_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello {full_name}\n")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
   
        
        
person_one = User("john", "hwang", 25, 91801)
person_one.describe_user()
person_one.greet_user()
print(f"{person_one.first_name} has tried to log in: {person_one.login_attempts} times!")
person_one.increment_login_attempts()
person_one.increment_login_attempts()
person_one.increment_login_attempts()
print(f"{person_one.first_name} has tried to log in: {person_one.login_attempts} times!")