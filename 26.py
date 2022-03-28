import json
from collections import *

a = {}
a['re'] = 're'
a[1] = 1
# a[4] = 4
print(a)
with open("qwer.json", 'w') as f:
    json.dump(a, f)
with open("qwer.json", 'r+') as f:
    print(json.load(f))

# di = OrderedDict()
# di[1] = 1
# di[2] = 2
#
# di_2 = OrderedDict()
# di_2[2] = 2
# di_2[1] = 1
# print(di == di_2)
