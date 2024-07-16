from pathlib import Path

path = Path('chapter_10/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()
print("printing contents:")
print(f"\n{contents}")

print("\nprinting lines:")
for line in lines:
    print(line)