# 8-3. T-Shirt: 
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.

def make_shirt(size, message):
    print(f"The size of the shirt will be: {size}")
    print(f"It will say: {message}")

make_shirt("large", "Muay-Thai!")
make_shirt(message="I Love Pie", size="small")