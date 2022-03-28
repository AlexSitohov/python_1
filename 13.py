import json

dict_1 = {i: i + 10 for i in (range(0, 11))}
# print(dict_1)
# ff = json.dumps(dict_1)
# print(ff)
# print(json.loads(ff))

with open('json_test.json', 'w') as f:
    json.dump(dict_1, f)

with open('json_test.json', 'r') as f:
    print(json.load(f))
