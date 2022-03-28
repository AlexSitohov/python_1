from collections import *

# # Работа с tuples


# def first():
#     try:
#         t = (123, 41, 4, 1, 4, 1)
#         # t[1] = 3
#         print(id(t))
#         print(t.__add__((4,54,5)),id(t.__add__((4,54,5))))
#     except Exception as e:
#         print(f'Ошибка - {e}')
#
#
# first()


# named tuples.
# Классы???


# player = namedtuple('player', 'name age rating')
# players = [player('Sandrik', 21, 9999), player('Alex', 21, 0000), player('Batik', 21, 5000)]
# print(players[1].name)
# print(players[1].age)
# print(players[1].rating)
# print(type(player))

# sum = 0
# Numbers = namedtuple('Numbers', ['x', 'y', 'z'])
# p = Numbers(10, 20, 30)
# for i in p:
#     sum += i
# print(sum,type(p))


# def pl():
#     player = namedtuple('player', 'age')
#     players = player(21)
#     print(players, type(players))
#
# def main():
#     pl()
#
# if __name__ == '__main__':
#     main()


# a = namedtuple('Something', ('x', 'y', 'z', 'w', 'c'))
# b = a(3131, 31, [1, 2, 3, 4, 5], 'four', 'five')
# print(b, type(b))

a = namedtuple('Something', {'x', 'y'})
b = a(1, 30)
print(b,type(b))










# player = namedtuple('player', 'name age rating')
# players = player('Sandrik', 21, 9999)
# print(players.age)