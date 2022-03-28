import random
import sys

# a = int(input('кол-во - '))
# for i in range(1, a + 1):
#     print('*' * i)


# a = int(input('кол-во - '))
# b = [i for i in range(0, a + 1)]
# for i in b:
#     if i % 2 == 0:
#         print(f'четное - {i}')
#     else:
#         print(f'нечетное - {i}')


# limit = int(input())
# a = [i for i in range(0, limit + 1) if i % 3 == 0 or i % 5 == 0]
# print(sum(a))


# first_lst = sys.argv[1]
# second_lst = sys.argv[2]


# ваше решение ниже:
# b = []
# a = [[i, ii] for i in range(0, 10) for ii in range(0, 10) if i % 2 != 0 and ii % 2 == 0]
# for i in a:
#     b.extend(i)
# c = set(b)
# print(list(c))


# test = [2, 3, 4, 10, 'Q', 5]
# card_dict = {2: 1,
#              3: 1,
#              4: 1,
#              5: 1,
#              6: 1,
#              7: 0,
#              8: 0,
#              9: 0,
#              10: -1,
#              'J': -1,
#              'Q': -1,
#              'K': -1,
#              'A': -1
#              }
# count = 0
# for i in test:
#     for ii in card_dict:
#         if i == ii:
#             count += card_dict[ii]
# print(count)


# table_cards = ['3_S', '10_H', '10_D', '10_C', '10_S']
# hand_cards = ['3_S', '4_D']
# all_cards = []
# for i in table_cards:
#     all_cards.append(i[-1])
# for i in hand_cards:
#     all_cards.append(i[-1])
# print(all_cards)
# if all_cards.count('S') >= 5:
#     print("Flush!")
# elif all_cards.count('H') >= 5:
#     print("Flush!")
# elif all_cards.count('D') >= 5:
#     print("Flush!")
# elif all_cards.count('C') >= 5:
#     print("Flush!")
# else:
#     print("No Flush")
#

# Угадывание числа
# a = random.randint(1, 51)
# count = 0
# while count !=6:
#     b = int(input('ваша попытка - '))
#     if b == a:
#         print('Угадано')
#         break
#     else:
#         if a > b:
#             print('Больше')
#         else:
#             print('Меньше')
#     count+=1


# Камень ножницы бумага
lst = ['Ножницы', 'Бумага', 'Камень']
v = 0
l = 0
n = 0
while True:
    print(f'Побед - {v}, Поражений - {l}, Ничьих - {n}')
    a = random.choice(lst)

    b = input('Ваш ход - ')
    print(f'Ход Компьютера - {a}')
    if b == 'Ножницы' and a == 'Бумага':
        print('Победа')
        v += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Ножницы' and a == 'Камень':
        print('Поражение')
        l += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Ножницы' and a == 'Ножницы':
        print('Ничья')
        n+=1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Бумага' and a == 'Ножницы':
        print('Поражение')
        l += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Бумага' and a == 'Камень':
        print('Победа')
        v += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Бумага' and a == 'Бумага':
        print('Ничья')
        n += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Камень' and a == 'Ножницы':
        print('Победа')
        v += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Камень' and a == 'Бумага':
        print('Поражение')
        l += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
    elif b == 'Камень' and a == 'Камень':
        print('Ничья')
        n += 1
        b = (input('Хотите сыграть еще? '))
        if b == 'нет':
            break
