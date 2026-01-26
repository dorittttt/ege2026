# from math import dist
# f = open(r"C:\Users\Misha\AppData\Local\Education\PythonProject\Ege\homework variantik 25093318\27_A_21425.txt")
#
# data =[[float(i) for i in row.replace(",",'.').split()]for row in f]
#
# claster1 = []
# claster2 = []
#
# for x, y in data:
#     if 15 < x < 32 and 15 < y < 32:
#         claster1.append([x, y])
#     if 0 < x < 15 and -20 < y < 0:
#         claster2.append([x, y])
#
# def find_Center(claster):
#     center = None
#     summa_rast = 10**9
#     for start in claster:
#         temp = 0
#         for stop in claster:
#             temp += dist(start, stop)
#         if temp < summa_rast:
#             center = start
#             summa_rast = temp
#
#     return center
#
# x1, y1 = find_Center(claster1)
# x2, y2 = find_Center(claster2)
#
# print(int((x1 + x2) / 2 * 10000))
# print(int((y1 + y2) / 2 * 10000))
from math import dist
f = open(r"C:\Users\Misha\AppData\Local\Education\PythonProject\Ege\homework variantik 25093318\27_B_21425.txt")

data =[[float(i) for i in row.replace(",",'.').split()]for row in f]

claster1 = []
claster2 = []
claster3 = []

for x, y in data:
    if -15 < x < 0:
        claster1.append([x, y])
    elif 5 < x < 25 and 10 < y < 30:
        claster2.append([x, y])
    elif 20 < x < 35 and -20 < y < 0:
        claster3.append([x, y])

def find_Center(claster):
    center = None
    summa_rast = 10**9
    for start in claster:
        temp = 0
        for stop in claster:
            temp += dist(start, stop)
        if temp < summa_rast:
            center = start
            summa_rast = temp

    return center

x1, y1 = find_Center(claster1)
x2, y2 = find_Center(claster2)
x3, y3 = find_Center(claster3)

print(int((x1 + x2 + x3) / 3 * 10000))
print(int((y1 + y2 + y3) / 3 * 10000))
