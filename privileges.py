# 2024-07-12 11:30:45
class User:
    def __init__(self, first_name, last_name, age, zip_code, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.zip_code = zip_code
        self.login_attempts = 0
        
    def describe_user(self):
        print("User: ")
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

class Admin(User):
    def __init__(self, first_name, last_name, age, zip_code, login_attempts):
        super().__init__(first_name, last_name, age, zip_code, login_attempts)
        self.privileges = Privileges()
        

            
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges 
    
    def show_privileges(self):
        print("These are the following privileges of an admin: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f" -{privilege}")
        else:
            print("user has no privileges")
            
me = Admin("john", "hwang", 25, 91801,0)
me.describe_user()
me.privileges.show_privileges()

privileges_list = ["can add post", "can delete post", "can bad user"]
me.privileges.privileges = privileges_list
me.privileges.show_privileges()