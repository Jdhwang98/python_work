active = True
message = "please enter a pizza toping: "
while True:
    topping = input(message)
    if topping != "quit":
        print(f"{topping} will be added to your pizza!")
    else:
        print("exiting program!")