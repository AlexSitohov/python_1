import os
import shutil

way = 'C:\\Users\merc\Desktop\level1'


def level_walker(way, level=1):
    for file in os.listdir(way):
        print(way, f'level is ------- {level}')
        if os.path.isdir(way + '\\' + file):
            print(os.listdir(way))
            print(f'go to {way} \\ {file}')
            level_walker(way + '\\' + file, level=level + 1)
            print(f'go back to {way}')


level_walker(way)
