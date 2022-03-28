import os

fff = []
way = 'C:\\Users\merc\Desktop\level1'
for p, d, f in os.walk(way):
    fpath = [os.path.join(p, file) for file in f if file.endswith('.txt')]
    fff.extend(fpath)
print(fff)

print(os.path.exists('result'))
