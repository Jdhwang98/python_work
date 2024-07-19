guest_list = ["eryn", "rona", "susie"]
message = f"{guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} are still coming over for dinner"
print(message)

message = f"There's actually a larger table I will invite more people"
print(message)

guest_list.insert(0,"fred")
guest_list.insert(2,"cathy")
guest_list.append("carolyn")

message = f"Here is who is going now: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]},{guest_list[4]}, {guest_list[5]}"
print(message)