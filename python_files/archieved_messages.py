# 2024-07-11 02:02:14
# 8-11. Archived Messages: 
# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function,
# print both of your lists to show that the original list has retained its messages.

text_messages = ["i want to eat pizza today", "let's go to the beach", "we are going to watch a movie today", "the gym is fun"]
sent_messages = []

def show_messages(text_messages):  
    for message in text_messages:
        print(f"\n{message}")

def send_message(text_messages, sent_messages):
    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    print(f"\n{sent_messages}")

show_messages(text_messages)
send_message(text_messages[:], sent_messages)
print(text_messages)
