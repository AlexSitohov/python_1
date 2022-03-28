import os
import shutil

a = 'C:\\Users\merc\Desktop\level1'


def leveler(a, level=1):
    print('level = ', level, a)
    for i in os.listdir(a):
        if os.path.isdir(a + '\\' + i):
            print('go', a + '\\' + i)
            leveler(a + '\\' + i, level + 1)
            if i == 'target':
                print(a + '\\' + i, 'Цель найдена!')
            print('back', a)


leveler(a)
