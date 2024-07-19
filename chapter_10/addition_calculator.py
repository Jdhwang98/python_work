while True: 
    try:
        x = input("enter a number: ")
        if x == "quit":
            print("ending program")
            break
        x = int(x)
        
        y = input ("enter another number: ")
        if x == "quit":
            print("ending program")
            break
        y = int(y)
    except ValueError:
        print("please only input numbers")
    else:
        sum = x + y
        print(f"The sum of {x} + {y} = {sum}\n")    