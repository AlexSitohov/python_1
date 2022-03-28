result_dict = {}
with open('users.txt', 'r', encoding='utf8') as f, \
        open('hobby.txt', 'r', encoding='utf8') as g:
    for line in f:
        key = line.replace('\n', ' ').replace(',', ' ')
        value = g.readline().replace('\n', ' ').replace(',', ', ')
        if value == '':
            value = None
        result_dict[key] = value
    if g.readline() != '':
        print(result_dict)
        exit(1)
print(result_dict)

with open('result.txt', 'w', encoding='utf8') as w:
    w.write(str(result_dict))

with open('result.txt', 'r', encoding='utf8') as w:
    print(w.read())
    print(w.tell())
