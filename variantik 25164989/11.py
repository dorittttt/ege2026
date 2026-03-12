from math import *
alf = 10 + 52 + 34

for x in range(1, 1000):
    i = ceil(log2(alf))
    if (
            (x * i) / 8 * 1141 > 305 * 1024
    ):
        print(x)
        break