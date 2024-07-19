user_name = []
if user_name:
    for user in user_name:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find more users!")