from itertools import islice


def first(s):
    for i in range(1, s + 1, 2):
        yield i


print(*islice(first(15), 10), sep='\n')
