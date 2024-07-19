#johnathan hwang 2024-06-27 10:12:44

# this is the main list of places to go
travel_list = ["norway", "sweden", "japan", "korea","germany"]
message = f"this is the places I want to go to: {travel_list}"
print(message)

# this is to sort only temp
message = f"this is a tempory sorted list {sorted(travel_list)}"
print(message)

message = f"but the original list is not changed: {travel_list}"
print(message)

# this is a temp reverse sort
message = f"this is the list in reverse alphabetical order:{sorted(travel_list,reverse=True)}"
print(message)

message = f"but the original list is not changed: {travel_list}"
print(message)


# reverse
print("reverse order:")
travel_list.reverse()
print(travel_list)

# reverse it back to normal
print("ordered")
travel_list.reverse()
print(travel_list)

# sort
print("sorted:")
travel_list.sort()
print(travel_list)

# reverse sort
print("reverse order:")
travel_list.sort(reverse=True)
print(travel_list)