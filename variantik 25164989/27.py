# f = open(r"27A_27780.txt")
# data = [[float(i) for i in row.replace(",",".").split()] for row in f]
#
# claster1 = []
# claster2 = []
#
# for x, y in data:
#     if 2 <= x <= 10 and 5 <= y <= 11.5:
#         claster1.append([x, y])
#     if 5 <= x <= 11 and 17 <= y <= 24:
#         claster2.append([x, y])
# from math import dist
#
# def find_center(claster):
#     center = None
#     rast = 10**10
#     for start in claster:
#         temp_rast = 0
#         for stop in claster:
#             temp_rast += dist(start, stop)
#         if temp_rast <= rast:
#             center = start
#             rast = temp_rast
#     return center
# center1 = (find_center(claster1))
# center2 = (find_center(claster2))
# print(len(claster1))
# print(len(claster2))
# rast1 = (dist(
#     center2, (1.0, 1.5)
# ))
# rast2 = (dist(
#     center1, (1.0, 1.5)
# ))
# print((rast1 + rast2) * 10000)

f = open(r"27B_27780.txt")
data = [[float(i) for i in row.replace(",",".").split()] for row in f]

claster1 = []
claster2 = []
claster3 = []

for x, y in data:
    if 14 <= x <= 21 and 23 <= y <= 32:
        claster1.append([x, y])
    if 16 <= x <= 24 and 13 <= y <= 21:
        claster2.append([x, y])
    if 25 <= x <= 31 and 11 <= y <= 20:
        claster3.append([x, y])
from math import dist

def find_center(claster):
    center = None
    rast = 10**10
    for start in claster:
        temp_rast = 0
        for stop in claster:
            temp_rast += dist(start, stop)
        if temp_rast <= rast:
            center = start
            rast = temp_rast
    return center
def count_12(claster, center):
    k = 0
    for start in claster:
        if start != center:
            if dist(start, center) <= 1.2:
                k += 1
    return k

# print(len(claster2))

# print(count_12(claster2, find_center(claster2)))

def min_ratt(claster, center):
    min_rast = 10**10
    for start in claster:
        if start != center:
            min_rast = min(min_rast, dist(start, center))
    return min_rast



print(len(claster1))
print(min_ratt(claster1, find_center(claster1)) * 10000)