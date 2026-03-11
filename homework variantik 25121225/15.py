from itertools import *

p = range(10, 1000 + 1)
q = range(27, 2222 + 1)

coords = combinations(sorted([10, 1000, 27, 2222]), r = 2)
dlini = set()

for start, stop in coords:
    a = range(start, stop + 1)
    flag = True
    for x in range(1, 1000):
        if not(
                (not(x in a)) or (((x in p) == (x in q)) <= (not(x in a)))
        ):
            flag = False
    if flag:
        dlini.add(stop - start)
print(min(dlini))