pizzas = ["cheese", "bbq", "supreme"]
friend_pizzas = pizzas[:]

pizzas.append("white")
friend_pizzas.append("onion")

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
