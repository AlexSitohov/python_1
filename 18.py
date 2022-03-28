import os
import shutil

way = 'C:\\Users\merc\Desktop\level1'


def le(way):
    print(way)
    for i in os.listdir(way):
        if os.path.isdir(way + '\\' + i):

            print('go', way + '\\' + i)
            le(way + '\\' + i)
            print('back', way)
        else:
            print(os.listdir(way))


le(way)
