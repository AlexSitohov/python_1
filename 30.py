from datetime import *

start = datetime.now()
a = [i for i in range(100)]
result = [(x, y, z, w) for x in a for y in a for z in a for w in a if abs(x - y - z - w) == 0]
print(*result, len(result), sep='\n')
end = datetime.now()
print(f'{abs(start - end)}')
