from pathlib import Path
import json

numbers = [2, 3, 5, 1, 0, 13]

path = Path("chapter_10/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)