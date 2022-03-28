'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
'''


def first(a):
    for i in range(1, a + 1, 2):
        yield i


second = first(15)
etie = 1
for i in range(1, 16, 2):
    print(next(second))
    etie += 2
print()


def nums(gt):
    return (i for i in range(1, gt + 1, 2))


ooo = nums(15)
hhh = 1
for i in range(1, 16, 2):
    print(next(ooo))
    hhh += 2

gg = (i for i in range(1, 16) if i % 2 != 0)
print(*gg)
