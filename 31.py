lst = []
lst_2 = []
g = 0
for i in range(int(input('введите число '))):
    gen = [a for a in range(100)]
    for ii in gen:
        lst.append(ii)
        lst_2.append(ii)
for y in lst:
    for yy in lst_2:
        for yyy in lst_2:
            if abs(y - yy - yyy) == 0:
                print(y, yy, yyy)
