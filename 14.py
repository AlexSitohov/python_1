import json

main_dict = {}
with open('users.txt', 'r', encoding='utf8') as f, \
        open('hobby.txt', 'r', encoding='utf8') as g, \
        open('result.txt', 'w', encoding='utf8') as q:
    for line in f:
        key = line.replace('\n', '').replace(',', ' ')
        value = g.readline().replace('\n', ' ')
        if value == '':
            value = None
        main_dict[key] = value
    if g.readline() != '':
        print(main_dict)
        print(1)
    json.dump(reas)

print(main_dict)
