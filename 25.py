# работа со словарями.
dictionary = {i: i ** 2 for i in range(10)}
# for key in dictionary.keys():
#     values = dictionary.get(key)
#     print(values)
del dictionary[5]
print(dictionary)
for key in dictionary.keys():
    values = dictionary.get(key)
    print(f'values - {values}')

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print((list(dictionary.keys())))
print(list(dictionary.values()))
print(list(dictionary.items()))
for i, ii in dictionary.items():
    print(i, ii)
