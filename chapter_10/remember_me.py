from pathlib import Path
import json

def greet_user():
    username = input("what is your name? ")
    path = Path("chapter_10/username.json")
    contents = json.dumps(username)
    path.write_text(contents)

    print(f"we'll remember you when you come back {username}!")
    
greet_user()