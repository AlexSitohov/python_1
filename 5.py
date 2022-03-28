# еще 1 функция генератора
import time


def gen():
    for i in range(1, 11):
        time.sleep(0.5)
        yield i


lst = []
for g in gen():
    print(f'шаг - {g}')
    print(g)
    lst.append(g)
print(f'Список - {lst}')
