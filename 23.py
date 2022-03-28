# def first(x, count=0):
#     # while x - 6 >= 0:
#     #     x -= 6
#     #     count += 1
#     count = int(x / 6)
#     return count
#
#
# print(first(int(input('колво кофе - '))))


# def way(x, y):
#     print(f'{abs(x - y):1.3}')
#
#
# way(5.0, 10)


def second(x, y, z):
    try:
        print(x * 2 + y * 4 + z * 4)
    except Exception as e:
        return (f'Ошибка {e}')
    else:
        return 'все норм'
    finally:
        print('End')


print(second(10, 10, 10))
