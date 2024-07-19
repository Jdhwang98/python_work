import os
import shutil


"""
_summary_
program that moves all specified file
extensions to a directory of choice
"""
    
files = [f for f in os.listdir() if '.py' in f.lower()]

os.mkdir('python_files')

for file in files:
    new_path = 'python_files/' + file
    shutil.move(file, new_path)