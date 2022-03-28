a = [i for i in range(1, 11)]
b = {}
# print(a)
for o in enumerate(a, 1):
    b.setdefault(o[0], o)
print(b)
