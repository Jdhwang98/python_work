
while True:
    response = input("How old are you?: ")
    if response == "quit":
        break

    response = int(response)
    if response < 3:
        print("your ticket is free")
    elif response < 12:
        print("your ticket is $10")
    else: 
        print("your ticket is $15")