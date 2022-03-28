import os

way = 'C:\\Users\merc\Desktop\level1'
for i in os.scandir(way):
    if isinstance(i, os.DirEntry):
        if i.is_dir():
            print(i.name, os.path.abspath(i.path))

print(__file__)
print(os.curdir)
print(os.path.abspath(os.curdir))