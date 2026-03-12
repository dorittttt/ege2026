from itertools import product
from string import digits
alf = digits[:7]
# print(len(alf))
k = 0
for i in product(alf, repeat = 5):
    num = ''.join(i)
    if num[0] != "0" and num.count("0") == 1 and num.count("1") <=2:
        k += 1
print(k)

