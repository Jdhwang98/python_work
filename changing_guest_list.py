guest_list = ["eryn", "rona", "susie"]
message = f"Hey {guest_list[0].title()}, want to come over for dinner?"
print(message)

message = f"Hey {guest_list[1].title()}, want to come over for dinner?"
print(message)

message = f"Hey {guest_list[2].title()}, want to come over for dinner?"
print(message)

removed_person = guest_list.pop()
message = f"{removed_person.title()} can't make it to the dinner party!"
print(message)

guest_list.append("jaxson")
message = f"It's okay, {guest_list[2].title()} took {removed_person.title()}'s spot"
print(message)

message = f"{guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} are still coming over for dinner"
print(message)