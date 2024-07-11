current_users = ["john", "eryn", "jaxson", "fred", "rona"]
new_users = ["greg", "max", "jaxson", "fred", "ayinde"]

for user in new_users:
    if user in current_users:
        print(f"sorry, {user} already exists in the system")
    else:
        print(f"welcome {user}!")


