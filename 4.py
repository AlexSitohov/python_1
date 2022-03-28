# два вида условий в генераторных выражениях.
a = (i if i < 5 else "skrt" for i in range(10))

print(*a, end=' ')
print()
b = (i for i in range(10) if i < 5)
print(*b, end=' ')
