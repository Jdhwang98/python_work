from pathlib import Path
import json


path = Path("chapter_10/favorite_number.json")

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number}")
else:
    favorite_number = input("Please enter favorite number: ")
    content = json.dumps(favorite_number)
    path.write_text(content)