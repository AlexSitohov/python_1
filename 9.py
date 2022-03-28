def first(i):
    return i ** 2


f = [first(i) for i in range(10)]
# print(list(map(first,f)))
print(f)
