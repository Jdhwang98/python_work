sandwich_orders = ["blt", "tuna melt", "italian", "ham and swiss"]
finished_sanwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"working on {current_sandwich}")
    finished_sanwiches.append(current_sandwich)
for sandwich in finished_sanwiches:
    print(f"Your {sandwich} is done!")
