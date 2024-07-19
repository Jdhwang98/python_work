# 2024-07-18 12:34:20
from pathlib import Path
import json

def get_current_user(path):
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None   
    
def get_new_user(path):
    username = input("please enter username: ")
    favorite_game = input("please enter your favorite game: ")
    favorite_color = input("please enter favorite color: ")
    
    user_dict = {
        "username" : username,
        "favorite_game" : favorite_game,
        "favorite_color" : favorite_color,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    path = Path("chapter_10/user_dict.json")
    user_dict = get_current_user(path)
    if user_dict:
        correct = input(f"Are you: {user_dict["username"]}, (y/n)")
        if correct == 'y':
            print(f"Welcome back {user_dict["username"]}!")
            print(f"Your favorite game is {user_dict["favorite_game"]}!")
            print(f"And your favorite color is {user_dict["favorite_color"]}!")
        else:
            user_dict = get_new_user(path)
            print(f"I will remember who you are next time, {user_dict["username"]}!")
    else:
        user_dict = get_new_user(path)
        print(f"I will remember who you are next time, {user_dict["username"]}!")
        

greet_user()


