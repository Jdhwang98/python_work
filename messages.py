# 2024-07-10 20:46:54

# 8-9. Messages: 
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), 
# which prints each text message.

text_messages = ["i want to eat pizza today", "let's go to the beach", "we are going to watch a movie today", "the gym is fun"]

def show_messages(text_messages):  
    for message in text_messages:
        print(message)

show_messages(text_messages)
