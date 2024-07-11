# 2024-07-11 03:36:57
# 8-12. Sandwiches: 
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

def make_sandwich(*items):
    print("ready to make your sandwhich!")
    for item in items:
        print(f" - adding {item} to your sandwich")
    print("sandwich is all done!\n")

make_sandwich("bacon", "tomatoe", "lettuce", "ham")
make_sandwich("egg", "bacon", "potato")