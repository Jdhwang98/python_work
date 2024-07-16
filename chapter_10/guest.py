from pathlib import Path
path = Path('chapter_10/guest.txt')
message = "Hello what is your name?"
message += "Enter 'quit' if you would like to end program: "
guest_names = []
while True:
    guest_name = input(message)
    if guest_name == 'quit':
        break
    
    print(f"thank you {guest_name} you have been added to the guest book")
    guest_names.append(guest_name)
    
file_string = ''
for name in guest_names:
    file_string += f"{name.lower()}\n"
path.write_text(file_string)

content = path.read_text().title()
print(content)