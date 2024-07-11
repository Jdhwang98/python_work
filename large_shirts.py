# 8-4. Large Shirts: 
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(message="I LOVE CODE!!!", size= "large"):
    print(f"The size of the shirt will be: {size}")
    print(f"It will say: {message}")

make_shirt("large", "Muay-Thai!")
make_shirt(message="I Love Pie", size="small")
make_shirt("kick-ass!")
make_shirt()