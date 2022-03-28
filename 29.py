# перебор чисел в 4 списках при разности которых получаем 0.
from datetime import *

start_time = datetime.now()

a = [y for y in range(100)]
count = 0
for i in a:
    for ii in a:
        for iii in a:
            for iiii in a:
                if abs(i - ii - iii - iiii) == 0:
                    # print(f'четыре числа - {i}, {ii}, {iii}, {iiii} дают при вычитании 0')
                    count += 1
print(f'количество комбинаций - {count}')
end_time = datetime.now()
print(f'Duration: {end_time - start_time}')
