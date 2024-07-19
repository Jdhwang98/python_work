from pathlib import Path

filenames = ["chapter_10/cats.txt", "chapter_10/dogs.txt"]

for filename in filenames:
    print(f"\nreading files from {filename}")
    path = Path(filename)
    
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("The file could not be found")
    else:
        print(f"{contents}\n")
    
    
#     filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
#     print(f"\nReading file: {filename}")

#     path = Path(filename)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         print("  Sorry, I can't find that file.")
#     else:
#         print(contents)