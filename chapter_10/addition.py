try:
    x = input("enter a number: ")
    x = int(x)
    
    y = input ("enter another number: ")
    y = int(y)
except ValueError:
    print("please only input numbers")
else:
    sum = x + y
    print(f"The sum of {x} + {y} = {sum}")    
        
        
