with open('zxc moves.txt', 'r+') as f:
    for line in f:
        print(line.replace('\n', ''))

    print(f.tell())
