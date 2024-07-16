from pathlib import Path

path = Path('chapter_10/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()


print("\nprinting lines:")
for line in lines:
    line = line.replace('python', 'C++')
    print(line)