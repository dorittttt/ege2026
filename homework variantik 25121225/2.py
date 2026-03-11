from itertools import *

def f(x, y, w, z):
    return (y <= x) and (not(z <= (x == w)))

for a in product([0,1], repeat = 7):
    table = [
        (0, a[0], a[1], 0),
        (1, a[2], a[3], a[4]),
        (a[5], 0, a[6], 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p, sep='')