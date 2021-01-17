#!/usr/bin/env python3

import os
from pathlib import Path
myFiles = ['accounts.txt','details.csv', 'invite.docx']

FILE_PATH = "/Users/justinthong/Documents/GitHub/automate-boring-stuff/python/reading-and-writing-files"

for filename in myFiles:
    print(Path(FILE_PATH))

print("justin")

print(str(Path('spam', 'bacon', 'eggs')))
print(Path('spam') /'bacon'/ 'eggs')
print(Path(r'spam')) # r means string is treated as raw string. meaning all escap codes are ignored
print(r'spam\neggs') # r means string is treated as raw string. meaning all escap codes are ignored
print('spam\neggs') 

print(Path.cwd())


# newpath = os.path.join(FILE_PATH, "new")
# os.makedirs(newpath)

newpath2 = Path( FILE_PATH) /'new2'
Path(newpath2).mkdir()

p = Path(FILE_PATH)
print(p.anchor)
