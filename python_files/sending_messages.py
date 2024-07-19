# 2024-07-10 21:05:45
# 8-10. Sending Messages: 
# Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() 
# that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, 
# print both of your lists to make sure the messages were moved correctly.

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
send_message(text_messages, sent_messages)