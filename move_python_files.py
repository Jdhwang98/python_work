import os
import shutil

files = [f for f in os.listdir() if '.py' in f.lower()]

os.mkdir('python_files')

for file in files:
    new_path = 'python_files/' + file
    shutil.move(file, new_path)