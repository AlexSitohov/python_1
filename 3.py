import sys


#
# b = {i for i in enumerate(range(1, 11),1)}
# print(type(b), sys.getsizeof(b))
#
#
# for i in b:
#     print(i)


def gen(num):
    for i in range(0, num + 1):
        yield i
    print('end')


gnum = gen(10)
count = 0
for i in range(0, 10):
    if count < 100:
        print(next(gnum))

# ty = [12123,1,3,13,1,3,1,23,21,3,13,12,3,1,3,13,1,1,1,1,1,1]
# tr = {o for o in ty}
# print(tr)
