class User:
    def __init__(self, first_name, last_name, age, zip_code, login_attempts):
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
print(f"{person_one.login_attempts}")
person_one.increment_login_attempts()
person_one.increment_login_attempts()
person_one.increment_login_attempts()
print(f"{person_one.login_attempts}")



person_two = User("eryn", "bollin", 30, 91800)
person_two.describe_user()
person_two.greet_user()

