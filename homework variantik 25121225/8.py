from itertools import *
k = 0
for i in product("0123456", repeat = 7):
    num = "".join(i)
    if num[0] == "0":
        continue
    for j in num:
        if int(j) % 2 == 0:
            num = num.replace(j, "*")
        if int(j) % 2 != 0:
            num = num.replace(j, "_")
    if num.count("*_") == 2:
        k += 1
print(k)